import { range, sum } from "lodash";
import { fileReader } from "../helpers/readfile";

const alignmentsRaw = fileReader("day7/input7_1.txt")();

const calcDiff = (diff: number) => (diff * diff + diff) / 2;
const calcDiffArray = (arr: number[]) =>
  arr.reduce((acc, diff) => acc + calcDiff(diff), 0);

const alignments = (alignmentsRaw || "")
  .split(",")
  .map((alignmentStr) => parseInt(alignmentStr));

let cost = 0;
let higherDiffs: number[] = [];
let lowerDiffs: number[] = [];
let numSame = 1;
let answer = alignments[0];
const nums = { [answer]: 1 };

// 16,1,2,0,4,2,7,1,2,14

alignments.shift();
alignments.forEach((curNum, i) => {
  const lower = curNum < answer;
  const higher = curNum > answer;
  const diff = Math.abs(curNum - answer);
  cost += calcDiff(diff);

  nums[curNum] = nums[curNum] || 0;
  nums[curNum]++;
  if (lower) {
    lowerDiffs.push(diff);
    let lowerDiffCosts = calcDiffArray(lowerDiffs.map((x) => x - 1));
    let higherDiffCosts = calcDiffArray(higherDiffs.map((x) => x + 1));

    while (lowerDiffCosts + higherDiffCosts + numSame < cost) {
      answer--;
      cost = lowerDiffCosts + higherDiffCosts + numSame;

      higherDiffs = higherDiffs.map((x) => x + 1);
      range(numSame).forEach((x) => higherDiffs.push(1));

      numSame = nums[answer] || 0;
      lowerDiffs = lowerDiffs.map((x) => x - 1).filter(Boolean);

      lowerDiffCosts = calcDiffArray(lowerDiffs.map((x) => x - 1));
      higherDiffCosts = calcDiffArray(higherDiffs.map((x) => x + 1));
    }
  } else if (higher) {
    higherDiffs.push(diff);
    let lowerDiffCosts = calcDiffArray(lowerDiffs.map((x) => x + 1));
    let higherDiffCosts = calcDiffArray(higherDiffs.map((x) => x - 1));

    while (lowerDiffCosts + higherDiffCosts + numSame < cost) {
      answer++;
      cost = lowerDiffCosts + higherDiffCosts + numSame;

      lowerDiffs = lowerDiffs.map((x) => x + 1);
      range(numSame).forEach((x) => lowerDiffs.push(1));

      numSame = nums[answer] || 0;
      higherDiffs = higherDiffs.map((x) => x - 1).filter(Boolean);

      lowerDiffCosts = calcDiffArray(lowerDiffs.map((x) => x + 1));
      higherDiffCosts = calcDiffArray(higherDiffs.map((x) => x - 1));
    }
  } else {
    numSame++;
  }
});

console.log(answer);
console.log(cost);
