import { sum } from "lodash";
import { fileReader } from "../helpers/readfile";

const startingFishRaw = fileReader("day6/input6_1.txt")();
const startingFishList = (startingFishRaw || "")
  .split(",")
  .map((fishStr) => parseInt(fishStr));

const spawnTime = 7;
const newFishDelay = 2;
const fishyAges = new Array(spawnTime + newFishDelay).fill(0);

startingFishList.forEach((fishAge) => fishyAges[fishAge]++);

let day = 0;
while (day++ < 80) {
  const numReadyFish = fishyAges.shift();

  // fish born
  fishyAges.push(numReadyFish);

  // fish restarting cycle
  fishyAges[spawnTime - 1] += numReadyFish;
}

console.log(fishyAges);
console.log(sum(fishyAges));
