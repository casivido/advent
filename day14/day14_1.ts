import { cloneDeep, forEach, map } from "lodash";
import { fileReader } from "../helpers/readfile";

const getNextLine = fileReader("day14/input14_1.txt");

const startingString = (getNextLine() || "").split("");

// skip blank line
getNextLine();

let line: string | false = false;
const rules: Record<string, string> = {};
while ((line = getNextLine())) {
  const [pair, insertion] = line.split(" -> ");
  rules[pair] = insertion;
}

let currentPairs: Record<string, number> = {};
let startingPair = "";
let endingPair = "";
let i = -1;
while (++i < startingString.length - 1) {
  const pair = startingString[i] + startingString[i + 1];
  if (i === 0) {
    startingPair = pair;
  }
  if (i === startingString.length - 2) {
    endingPair = pair;
  }

  currentPairs[pair] = (currentPairs[pair] || 0) + 1;
}

const steps = 40;
i = 0;
while (i++ < steps) {
  startingPair = startingPair[0] + rules[startingPair];
  endingPair = rules[endingPair] + endingPair[1];
  const prevPairs = currentPairs;
  currentPairs = {};

  forEach(prevPairs, (numPairs, pair) => {
    const newFirstPair = pair[0] + rules[pair];
    const newSecondPair = rules[pair] + pair[1];
    currentPairs[newFirstPair] = (currentPairs[newFirstPair] || 0) + numPairs;
    currentPairs[newSecondPair] = (currentPairs[newSecondPair] || 0) + numPairs;
  });
}

console.log(currentPairs);

const letterCounts: Record<string, number> = {
  [startingPair[0]]: 1,
  [endingPair[1]]: 1,
};

forEach(currentPairs, (numPairs, pair) => {
  letterCounts[pair[0]] = (letterCounts[pair[0]] || 0) + numPairs;
  letterCounts[pair[1]] = (letterCounts[pair[1]] || 0) + numPairs;
});

const mostCommon = {
  val: 0,
  letter: "",
};
const leastCommon = {
  val: Infinity,
  letter: "",
};
Object.keys(letterCounts).forEach((letter) => {
  const newValue = (letterCounts[letter] /= 2);
  if (newValue > mostCommon.val) {
    mostCommon.letter = letter;
    mostCommon.val = newValue;
  }
  if (newValue < leastCommon.val) {
    leastCommon.letter = letter;
    leastCommon.val = newValue;
  }
  return newValue;
});

console.log(letterCounts);
console.log(mostCommon);
console.log(leastCommon);
console.log(mostCommon.val - leastCommon.val);
