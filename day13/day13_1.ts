import { forEach } from "lodash";
import readFileByLine from "../helpers/readfile";

interface Instruction {
  axis: string;
  location: number;
}

// const mapByX: Record<number, number> = {};
// const mapByY: Record<number, number> = {};
let currentAxis: string = "x";
let points: Record<number, Record<number, boolean>> = {};
const instructions: Instruction[] = [];

const foldingMatchRegex = /fold along (\w+)=(\d+)/;
let readFoldingInstructions = false;
readFileByLine("day13/input13_test.txt", (line) => {
  if (line === "") {
    readFoldingInstructions = true;
  } else if (!readFoldingInstructions) {
    const [x, y] = line.split(",").map((str) => parseInt(str));
    if (!points[x]) {
      points[x] = {};
    }
    points[x][y] = true;
    // mapByX[x] = y;
    // mapByY[y] = x;
  } else {
    const [x, axis, location] = foldingMatchRegex.exec(line) || [];
    instructions.push({
      axis,
      location: parseInt(location),
    });
  }
});

// console.log(points);
// console.log(instructions);

instructions.forEach((instruction) => {
  const targetValue = instruction.location;
  const targetAxis = instruction.axis;

  forEach(points, (yRecord, xStr) => {
    let newPoint = false;
    let x = parseInt(xStr);
    if (targetAxis === "x" && x > targetValue) {
      newPoint = true;
      x = targetValue * 2 - x;
    }

    forEach(yRecord, (set, yStr) => {
      let y = parseInt(yStr);
      if (targetAxis === "y" && y > targetValue) {
        newPoint = true;
        y = targetValue * 2 - y;
      }

      if (newPoint) {
        if (!points[x]) {
          points[x] = {};
        }
        points[x][y] = true;
        delete points[parseInt(xStr)][parseInt(yStr)];
      }
    });
  });
});

console.log(points);

let sum = 0;
forEach(points, (yRecord, xStr) => {
  sum += Object.keys(yRecord).length;
});

console.log(sum);
