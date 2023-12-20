import re
import copy
from functools import reduce
from helpers import loadFileByLine

import pprint
print = pprint.PrettyPrinter(indent=2).pprint

INPUT_FILE = "2023/inputs/day19_data.txt"

subRuleRegex = r"(\w)([<>])(\d*)"
# ruleLine ex: px{a<2006:qkq,m>2090:A,rfg}
def addRule(ruleLine, rules):
    name, ruleRaw = ruleLine.split("{")
    subRulesRaw = ruleRaw[0:-1].split(",")

    # subRulesRaw ex: ["a<2006:qkq","m>2090:A","rfg"
    def decodeRule(subRule):
        if ":" in subRule:
            conditional, successDestination = subRule.split(":")
            category, op, number = re.search(subRuleRegex, conditional).groups()
            return {
                "isDefault": False,
                "op": op,
                "category": category,
                "number": int(number),
                "successDestination": successDestination
            }
        else:
            successDestination = subRule
            return {
                "isDefault": True,
                "successDestination": successDestination
            }
                
    subRules = list(map(decodeRule, subRulesRaw))
    rules[name] = subRules

def parseInstructions():
    instructionsRaw = loadFileByLine(INPUT_FILE)
    rules = {}

    index = 0
    moreRules = True
    while(moreRules):
        line = instructionsRaw[index]
        if line == "":
            index += 1
            moreRules = False
            continue
        addRule(line, rules)
        index += 1

    # ignore remaining item instructions
    return rules

def getNewLimits(pathLimits, subRule):
    newTrueLimits = copy.deepcopy(pathLimits)
    newFalseLimits = copy.deepcopy(pathLimits)
    if subRule["isDefault"]:
        return newTrueLimits, newFalseLimits

    category = subRule["category"]
    op = subRule["op"]
    number = subRule["number"]

    min, max = pathLimits[category]
    match op:
        case '>': # item > number, item_max > number
            if max <= number:
                newTrueLimits = False
            else:
                newTrueLimits[category][0] = number + 1
            if min > number:
                newFalseLimits = False
            else:
                newFalseLimits[category][1] = number
        case '<': 
            if min >= number:
                newTrueLimits = False
            else:
                newTrueLimits[category][1] = number - 1
            if max < number:
                newFalseLimits = False
            else:
                newFalseLimits[category][0] = number

    return newTrueLimits, newFalseLimits

def runPathRule(path, rules):
    skipToDefault = False
    pathLimits = copy.deepcopy(path["limits"])
    rule = rules[path["nextRule"]]
    newPaths = []
    for subRule in rule:
        previouslySeen = copy.deepcopy(path["seenRules"])
        if subRule["isDefault"]:
            newPaths.append({
                "limits": pathLimits,
                "seenRules": previouslySeen,
                "nextRule": subRule["successDestination"]
            })
        elif not skipToDefault:
            newTrueLimits, newFalseLimits = getNewLimits(pathLimits, subRule)
            if newTrueLimits != False:
                newPaths.append({
                    "limits": newTrueLimits,
                    "seenRules": previouslySeen,
                    "nextRule": subRule["successDestination"]
                })
            if newFalseLimits != False and pathLimits != False:
                pathLimits = newFalseLimits
            else:
                skipToDefault = True

    return newPaths

def getItemValue(item):
    return sum(item.values())

def getBlankPathLimits():
    return {
        "x": [1,4000],
        "m": [1,4000],
        "a": [1,4000],
        "s": [1,4000]
    }

def rangeOverlaps(range1, range2):
    start1, end1 = range1
    start2, end2 = range2
    return end1 >= start2 and end2 >= start1

def main():
    rules = parseInstructions()
    paths = [{
        "limits": getBlankPathLimits(),
        "seenRules": ["in"],
        "nextRule": "in"
    }]
    acceptedPaths = []
    rejectedPaths = []

    while len(paths):
        potentialNewPaths = []
        for path in paths:
            potentialNewPaths.extend(runPathRule(path, rules))

        newPaths = []
        for potentialNewPath in potentialNewPaths:
            nextRule = potentialNewPath["nextRule"]
            if nextRule == "A":
                acceptedPaths.append(potentialNewPath)
            elif nextRule == "R":
                rejectedPaths.append(potentialNewPath)
            else:
                if nextRule not in potentialNewPath["seenRules"]:
                    potentialNewPath["seenRules"].append(nextRule)
                    newPaths.append(potentialNewPath)
        paths = newPaths
    
    totalPossibilities = 0
    for path in acceptedPaths:
        pathLimits = path["limits"]
        pathPossibilities = reduce(lambda x,y: x*(y[1]-y[0]+1), pathLimits.values(), 1)
        totalPossibilities += pathPossibilities
        print(pathLimits)
        print(path["seenRules"])

    print(totalPossibilities)

main()