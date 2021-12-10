import readFileByLine from "../helpers/readfile";

let knownOutputs = 0;
readFileByLine("day8/input8_1.txt", (line: string) => {
  const [[...input], [...output]] = line
    .split("|")
    .map((side) => side.trim().split(" "));

  output.forEach((output) => {
    switch (output.length) {
      case 2:
      case 3:
      case 4:
      case 7:
        knownOutputs++;
        break;
    }
  });
});
console.log(knownOutputs);
