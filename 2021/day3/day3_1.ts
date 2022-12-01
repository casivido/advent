import readFileByLine from "../helpers/readfile";

const powers: number[] = [];

let bit: string;
let index = 0;
readFileByLine("day3/input3_1.txt", (line: string) => {
  index = 0;
  while ((bit = line[index])) {
    if (powers[index] === undefined) {
      powers.push(0);
    }

    powers[index] += bit === "1" ? 1 : -1;
    index++;
  }
});

let gamma = "";
let epsilon = "";
powers.forEach((rawPowerValue) => {
  gamma += rawPowerValue > 0 ? "1" : "0";
  epsilon += rawPowerValue < 0 ? "1" : "0";
});

console.log(gamma);
console.log("Gamma: ", parseInt(gamma, 2));

console.log(epsilon);
console.log("Epsilon: ", parseInt(epsilon, 2));

console.log("Final: ", parseInt(gamma, 2) * parseInt(epsilon, 2));
