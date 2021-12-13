import { isNumber, range } from "lodash";
import readFileByLine from "../helpers/readfile";

const map: number[][] = [];
readFileByLine("day11/input11_1.txt", (line) => {
  map.push(line.split("").map((numStr) => parseInt(numStr)));
});

let numFlashes = 0;
const increaseEnergy = (x: number, y: number) => {
  if (!isNumber(map?.[x]?.[y])) {
    return;
  }
  map[x][y]++;
  if (map[x][y] === 10) {
    numFlashes++;
    increaseEnergy(x - 1, y - 1);
    increaseEnergy(x, y - 1);
    increaseEnergy(x + 1, y - 1);
    increaseEnergy(x - 1, y);
    increaseEnergy(x + 1, y);
    increaseEnergy(x - 1, y + 1);
    increaseEnergy(x, y + 1);
    increaseEnergy(x + 1, y + 1);
  }
};

const resetEnergies = () => {
  let x = 0;
  let y = 0;
  let fullFlash = true;
  while (x < map.length) {
    while (y < map[0].length) {
      if (map[x][y] > 9) {
        map[x][y] = 0;
      } else {
        fullFlash = false;
      }
      y++;
    }
    y = 0;
    x++;
  }
  return fullFlash;
};

let stepNumber = 1;
const runStep = () => {
  let x = 0;
  let y = 0;
  while (x < map.length) {
    while (y < map[0].length) {
      increaseEnergy(x, y);
      y++;
    }
    y = 0;
    x++;
  }
  if (resetEnergies()) {
    console.log(stepNumber);
  }
  stepNumber++;
};

let index = 0;
while (index++ < 1000) {
  runStep();
}

// console.table(map);
console.log(numFlashes);
