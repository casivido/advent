import _ from "lodash";
import readFileByLine from "../helpers/readfile";

const powers: number[] = [];

let lines: string[] = [];
readFileByLine("day3/input3_1.txt", (line: string) => {
  lines.push(line);
});

const filterLines = (linesOG: string[], ruleFn: (val: number) => string) => {
  const lines = _.cloneDeep(linesOG);
  let prevBit: string | undefined;
  let bit = 0;
  while (lines.length > 1) {
    let value = 0;

    for (let index = 0; index < lines.length; ) {
      const line = lines[index];

      if (prevBit && prevBit !== line[bit - 1]) {
        lines.splice(index, 1);
        continue;
      }

      value += line[bit] == "1" ? 1 : -1;
      index++;
    }

    prevBit = ruleFn(value);
    bit++;
  }

  return lines[0];
};

const o2Number = filterLines(lines, (value) => (value >= 0 ? "1" : "0"));
const oxyNumber = filterLines(lines, (value) => (value < 0 ? "1" : "0"));
console.log(o2Number);
console.log(oxyNumber);

console.log(parseInt(o2Number, 2) * parseInt(oxyNumber, 2));
