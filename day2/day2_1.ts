import readFileByLine from "../helpers/readfile";

let depth = 0;
let position = 0;

const move = (direction: string, value: number) => {
  switch (direction) {
    case "forward":
      position += value;
      break;
    case "up":
      depth -= value;
      break;
    case "down":
      depth += value;
      break;
    default:
      break;
  }
};

readFileByLine(
  "day2/input1.txt",
  (line: string) => {
    const [direction, value] = line.split(" ");
    move(direction, parseInt(value));
  },
  (buf) => buf.toString()
);

console.log("depth: ", depth);
console.log("position: ", position);
console.log("X: ", position * depth);
