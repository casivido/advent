import readFileByLine from "../helpers/readfile";

let depth = 0;
let position = 0;
let aim = 0;

const move = (direction: string, value: number) => {
  switch (direction) {
    case "forward":
      position += value;
      depth = depth + aim * value;
      break;
    case "up":
      aim -= value;
      break;
    case "down":
      aim += value;
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
console.log("aim: ", aim);
console.log("X: ", position * depth);
