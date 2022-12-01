import { range } from "lodash";
import readFileByLine from "../helpers/readfile";

const map: Map = {};
let overlaps = 0;
readFileByLine("day5/input5_1.txt", (line: string) => {
  const [[x1, y1], [x2, y2]] = line
    .split(" -> ")
    .map((coords) => coords.split(",").map((num) => parseInt(num)));

  const yRange = range(Math.min(x1, x2), Math.max(x1, x2) + 1);
  const xRange = range(Math.min(y1, y2), Math.max(y1, y2) + 1);
  // console.log();
  // console.log(x1, y1, " -> ", x2, y2);
  // console.log(xRange);
  // console.log(yRange);

  const coordsHit =
    x1 === x2 || y1 === y2
      ? xRange.reduce<number[][]>(
          (acc, x) => acc.concat(yRange.map((y) => [x, y])),
          []
        )
      : xRange.map((x, i) => [
          x,
          (x1 < x2 && y1 > y2) || (x1 > x2 && y1 < y2)
            ? yRange[yRange.length - i - 1]
            : yRange[i],
        ]);
  // console.log(coordsHit);

  coordsHit.forEach(([x, y]) => {
    map[x] = map[x] || {};
    map[x][y] = map[x][y] || 0;

    map[x][y]++;
    if (map[x][y] === 2) {
      overlaps++;
    }
  });
});
// console.table(map);
console.log(overlaps);

type Map = Record<number, Record<number, number>>;
