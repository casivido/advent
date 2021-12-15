import { toInteger } from "lodash";
import readFileByLine from "../helpers/readfile";

const valueMap: Record<string, number> = {
  ")": 1,
  "]": 2,
  "}": 3,
  ">": 4,
};

const openCharMap: Record<string, string> = {
  "(": ")",
  "[": "]",
  "{": "}",
  "<": ">",
};
const openChars = Object.keys(openCharMap);

const closeCharMap: Record<string, string> = {
  ")": "(",
  "]": "[",
  "}": "{",
  ">": "<",
};

const values: number[] = [];
readFileByLine("day10/input10_1.txt", (line) => {
  const stack: string[] = [];
  const chars = line.split("");

  const valid = chars.every((char) => {
    if (openChars.includes(char)) {
      stack.push(char);
      return true;
    } else if (stack[stack.length - 1] === closeCharMap[char]) {
      stack.pop();
      return true;
    } else {
      return false;
    }
  });

  if (valid) {
    let value = 0;
    stack.reverse().forEach((lastChar) => {
      value *= 5;
      value += valueMap[openCharMap[lastChar]];
    });

    values.push(value);
  }
});

const sortedValues = values.sort((a, b) => b - a);
console.log(sortedValues[toInteger(sortedValues.length / 2)]);
