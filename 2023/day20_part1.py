import re
from queue import Queue
import copy
from functools import reduce
from helpers import loadFileByLine

import pprint
print = pprint.PrettyPrinter(indent=2).pprint

# Module Types
CONJ = "CONJ"
FLIP = "FLIP"
BROAD = "BROAD"
BUTTON = "BUTTON"

# Module Indices
TYPE = 0
DESTINATIONS = 1
STATE = 2

# Pulse Indices
SRC = 0
DEST = 1
INTENSITY = 2

# Intensity
LOW = "LOW"
HIGH = "HIGH"

# State
ON = True
OFF = False

INPUT_FILE = "2023/inputs/day20_data.txt"
MODULE_REGEX = "^([&%]?)(\w+) -> (.*)$"

def parseModuleLine(moduleLine):
    type, name, destinations = list(re.search(MODULE_REGEX, moduleLine).groups())
    if type == "":
        type = BROAD
    elif type == "%":
        type = FLIP
    elif type == "&":
        type = CONJ
    else:
        raise Exception("Unknown module type")
    
    destinations = destinations.split(", ")
    state = {} if type == CONJ else False
    return [name, type, destinations, state]

def parseInput():
    instructionsRaw = loadFileByLine(INPUT_FILE)
    moduleList = list(map(parseModuleLine, instructionsRaw))

    modules = {
        "button": [BUTTON, ["broadcaster"], None]
    }

    for module in moduleList:
        name, type, destinations, state = module
        modules[name] = [type, destinations, state]

    return modules

def runPulses(modules, pulsesQueue):
    pulseCounts = {
        LOW: 0,
        HIGH: 0
    }
    while pulsesQueue.qsize():
        sourceName, destName, pulseIntensity = pulsesQueue.get()
        pulseCounts[pulseIntensity] += 1

        if(destName not in modules):
            continue
        destModule = modules[destName]
        destType, destDestinations, destState = destModule
        if destType == BROAD:
            for newDestName in destDestinations:
                pulsesQueue.put([destName, newDestName, pulseIntensity])
        elif destType == FLIP:
            if pulseIntensity == HIGH:
                continue
            if destModule[STATE] == ON:
                for newDestName in destDestinations:
                    pulsesQueue.put([destName, newDestName, LOW])
            else: 
                for newDestName in destDestinations:
                    pulsesQueue.put([destName, newDestName, HIGH])
            destModule[STATE] = not destModule[STATE]
        elif destType == CONJ:
            destState[sourceName] = pulseIntensity
            allHigh = True
            for subState in destState.values():
                if subState == LOW:
                    allHigh = False
                    break
            if allHigh:
                for newDestName in destDestinations:
                    pulsesQueue.put([destName, newDestName, LOW])
            else:
                for newDestName in destDestinations:
                    pulsesQueue.put([destName, newDestName, HIGH])
    return pulseCounts

def initializeConjunctions(modules):
    for curName, curModule in modules.items():
        curDestinations = curModule[DESTINATIONS]
        for destName in curDestinations:
            if destName in modules:
                destType, destDestinations, destState = modules[destName]
                if destType == CONJ:
                    destState[curName] = LOW
        
# module format: [type, destinations, state]
# pulse format: [source, dest, instensity]
def main():
    modules = parseInput()
    initializeConjunctions(modules)
    startingPulse = ["button", "broadcaster", LOW]
    runsLeft = 1000

    pulseCountsList = []
    while runsLeft > 0:
        pulseQueue = Queue()
        pulseQueue.put(startingPulse)
        pulseCounts = runPulses(modules, pulseQueue)
        pulseCountsList.append(pulseCounts)
        runsLeft -= 1

    totalPulseCounts = {
        HIGH: 0,
        LOW: 0
    }
    for pulseCount in pulseCountsList:
        totalPulseCounts[HIGH] += pulseCount[HIGH]
        totalPulseCounts[LOW] += pulseCount[LOW]
    print(totalPulseCounts)
    print(totalPulseCounts[HIGH] * totalPulseCounts[LOW])



main()