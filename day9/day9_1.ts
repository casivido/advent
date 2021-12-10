import { sum } from "lodash";
import readFileByLine from "../helpers/readfile";

const map: number[][] = [];
readFileByLine("day9/input9_1.txt", (line: string) => {
  const newRow: number[] = [];
  line.split("").forEach((num) => newRow.push(parseInt(num)));
  map.push(newRow);
});

let startX = 0;
let startY = 0;

const lowPoints: number[] = [];
while (startX < map.length) {
  while (startY < map[0].length) {
    const x = startX;
    const y = startY;

    const height = map[x][y];

    const above = map?.[x]?.[y + 1];
    const below = map?.[x]?.[y - 1];
    const right = map?.[x + 1]?.[y];
    const left = map?.[x - 1]?.[y];

    let isLowest = true;
    if (
      (typeof above === "number" && above <= height) ||
      (typeof below === "number" && below <= height) ||
      (typeof left === "number" && left <= height) ||
      (typeof right === "number" && right <= height)
    ) {
      isLowest = false;
    }

    if (isLowest) {
      lowPoints.push(height + 1);
    }
    startY++;
  }
  startY = 0;
  startX++;
}
console.log(lowPoints);

console.log(sum(lowPoints));
