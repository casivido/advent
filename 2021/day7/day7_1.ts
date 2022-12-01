import { fileReader } from "../helpers/readfile";

const alignmentsRaw = fileReader("day7/input7_1.txt")();

const alignments = (alignmentsRaw || "")
  .split(",")
  .map((alignmentStr) => parseInt(alignmentStr));

let cost = 0;
let numHigher = 0;
let numLower = 0;
let numSame = 1;
let answer = alignments[0];
const nums = { [answer]: 1 };

// 16,1,2,0,4,2,7,1,2,14

alignments.shift();
alignments.forEach((curNum, i) => {
  const lower = curNum < answer;
  const higher = curNum > answer;
  cost += Math.abs(curNum - answer);

  nums[curNum] = nums[curNum] || 0;
  nums[curNum]++;
  if (lower) {
    numLower++;

    while (numLower > numHigher + numSame) {
      answer--;
      cost -= numLower;
      cost += numHigher + numSame;

      numHigher += numSame;
      numSame = nums[answer] || 0;
      numLower -= numSame;
    }
  } else if (higher) {
    numHigher++;

    while (numHigher > numLower + numSame) {
      answer++;
      cost += numLower + numSame;
      cost -= numHigher;

      numLower += numSame;
      numSame = nums[answer] || 0;
      numHigher -= numSame;
    }
  } else {
    numSame++;
  }
  if (numLower + numHigher + numSame !== i + 2) {
    console.log("WRONG");
  }
});

console.log(answer);
console.log(cost);
