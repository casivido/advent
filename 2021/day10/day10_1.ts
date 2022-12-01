import { sum } from "lodash";
import readFileByLine from "../helpers/readfile";

const valueMap: Record<string, number> = {
  ")": 3,
  "]": 57,
  "}": 1197,
  ">": 25137,
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

const brokenChars: string[] = [];
readFileByLine("day10/input10_1.txt", (line) => {
  const stack: string[] = [];
  const chars = line.split("");

  chars.every((char) => {
    if (openChars.includes(char)) {
      stack.push(char);
      return true;
    } else if (stack[stack.length - 1] === closeCharMap[char]) {
      stack.pop();
      return true;
    } else {
      brokenChars.push(char);
      console.log("broken v");

      return false;
    }
  });
  console.log(line);
});

console.log(brokenChars);

const answer = sum(brokenChars.map((char) => valueMap[char]));
console.log(answer);
