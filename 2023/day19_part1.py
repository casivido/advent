import re
from helpers import loadFileByLine

import pprint
print = pprint.PrettyPrinter(indent=2).pprint

subRuleRegex = r"(\w)([<>])(\d*)"
def getSubRuleFunction(category, op, number, successDestination):
    def doesItemSatisfySubRule(item):
        match op:
            case '<':
                return item[category] < number
            case '>':
                return item[category] > number
        raise Exception("Didn't find matching op")
    return doesItemSatisfySubRule

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
                "doesItemSatisfySubRule": getSubRuleFunction(category, op, int(number), successDestination),
                "successDestination": successDestination
            }
        else:
            successDestination = subRule
            return {
                "doesItemSatisfySubRule": lambda x: successDestination,
                "successDestination": successDestination
            }
                
    subRules = list(map(decodeRule, subRulesRaw))
    rules[name] = subRules

# itemLine ex: "{x=787,m=2655,a=1222,s=2876}"
def decodeItem(itemLine):
    x, m, a, s = re.findall(r'\b\d+\b', itemLine)
    return {
        "x": int(x),
        "m": int(m),
        "a": int(a),
        "s": int(s)
    }

def parseInstructions():
    instructionsRaw = loadFileByLine("2023/inputs/day19_data.txt")
    rules = {}
    items = []

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
    
    while(index < len(instructionsRaw)):
        line = instructionsRaw[index]
        items.append(decodeItem(line))
        index += 1

    return rules, items

def runRule(item, rule):
    for subRule in rule:
        if subRule["doesItemSatisfySubRule"](item):
            return subRule["successDestination"]
    raise Exception("No subrule satisfied")

def getItemValue(item):
    return sum(item.values())

def main():
    rules, items = parseInstructions()
    acceptedItems = []
    rejectedItems = []
    for item in items:
        nextRule = "in"
        result = None
        while result == None:
            nextRule = runRule(item, rules[nextRule])
            if nextRule == "A":
                result = "ACCEPTED"
                acceptedItems.append(item)
            elif nextRule == "R":
                result = "REJECTED"
                rejectedItems.append(item)
    print(acceptedItems)
    sum = 0
    for item in acceptedItems:
        sum += getItemValue(item)
    print(sum)
main()