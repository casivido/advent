import readlines from "n-readlines";

const input = new readlines("./input_1.txt");

let buffer = input.next();
if (!buffer) {
  throw new Error("Empty or invalid file.");
}

let numIncreases = 0;
let prevNumber = parseInt(buffer.toString());
while ((buffer = input.next())) {
  const curNumber = parseInt(buffer.toString());
  if (curNumber > prevNumber) {
    numIncreases++;
  }

  prevNumber = curNumber;
}

console.log("increases: ", numIncreases);
