import _ from "lodash";
import readlines from "n-readlines";

// const input = new readlines("./input_test.txt");
const input = new readlines("./input_1.txt");

let numIncreases = 0;
const nums = [];
for (let i = 0; i < 3; i++) {
  nums.push(parseInt(input.next().toString()));
}
let prevSum = _.sum(nums);

let buffer: Buffer | false;
while ((buffer = input.next())) {
  nums.shift();
  nums.push(parseInt(buffer.toString()));

  const curSum = _.sum(nums);
  if (curSum > prevSum) {
    numIncreases++;
  }

  prevSum = curSum;
}

console.log("Increases: ", numIncreases);
