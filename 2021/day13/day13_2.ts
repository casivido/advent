import { forEach, range } from "lodash";
import readFileByLine from "../helpers/readfile";

interface Instruction {
  axis: string;
  location: number;
}

let points: Record<number, Record<number, boolean>> = {};
const instructions: Instruction[] = [];

const foldingMatchRegex = /fold along (\w+)=(\d+)/;
let readFoldingInstructions = false;
let maxX = 0;
let maxY = 0;
readFileByLine("day13/input13_1.txt", (line) => {
  if (line === "") {
    readFoldingInstructions = true;
  } else if (!readFoldingInstructions) {
    const [x, y] = line.split(",").map((str) => parseInt(str));
    if (!points[x]) {
      points[x] = {};
    }
    points[x][y] = true;
    maxX = Math.max(x, maxX);
    maxY = Math.max(y, maxY);
  } else {
    const [x, axis, location] = foldingMatchRegex.exec(line) || [];
    instructions.push({
      axis,
      location: parseInt(location),
    });
  }
});

instructions.forEach((instruction) => {
  const targetValue = instruction.location;
  const targetAxis = instruction.axis;
  if (targetAxis === "x") {
    maxX = targetValue - 1;
  }
  if (targetAxis === "y") {
    maxY = targetValue - 1;
  }

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

let sum = 0;
forEach(points, (yRecord, xStr) => {
  sum += Object.keys(yRecord).length;
});

const display: string[] = [];
range(0, maxY + 1).forEach((y) => {
  display[y] = "";
  range(0, maxX + 1).forEach((x) => {
    display[y] += points?.[x]?.[y] ? "|" : " ";
  });
});

console.log(display);
