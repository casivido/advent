import { difference, forEach, intersection, invert } from "lodash";
import readFileByLine from "../helpers/readfile";

const NUMBERS = [
  "abcefg",
  "cf",
  "acdeg",
  "acdfg",
  "bcdf",
  "abdfg",
  "abdefg",
  "acf",
  "abcdefg",
  "abcdfg",
];

const getNumber = (output: string[], solution: Record<string, string>) => {
  const sortedOutput = output
    .map((letter) => solution[letter])
    .sort()
    .join("");

  return NUMBERS.findIndex((str) => str === sortedOutput);
};

let sums = 0;
readFileByLine("day8/input8_test.txt", (line: string) => {
  const seen: Record<number, string[][]> = {};
  const solution: Record<string, string> = {};
  const counts: Record<string, number> = {};

  const [[...inputs], [...outputs]] = line.split("|").map((side) =>
    side
      .trim()
      .split(" ")
      .map((input) => input.split(""))
  );

  inputs.forEach((input) => {
    input.forEach((letter) => (counts[letter] = (counts[letter] || 0) + 1));

    seen[input.length] = [...(seen[input.length] || []), input];
  });

  solution["a"] = difference(seen[3][0], seen[2][0])[0];
  solution["c"] = counts[seen[2][0][0]] === 8 ? seen[2][0][0] : seen[2][0][1];
  solution["f"] = difference(seen[2][0], [solution["c"]])[0];

  forEach(counts, (count, letter) => {
    if (count === 6) {
      solution["b"] = letter;
    } else if (count === 4) {
      solution["e"] = letter;
    }
  });

  solution["g"] = difference(
    intersection(...seen[6]),
    Object.values(solution)
  )[0];
  solution["d"] = difference(seen[7][0], Object.values(solution))[0];

  const invertedSolution = invert(solution);
  let curNum = 0;
  outputs.forEach(
    (output) => (curNum = curNum * 10 + getNumber(output, invertedSolution))
  );
  console.log(curNum);

  sums += curNum;
});

console.log(sums);
