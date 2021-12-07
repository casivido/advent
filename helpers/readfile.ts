import readlines from "n-readlines";

const readFileByLine = (filename, lineFn) => {
  const input = new readlines("./input_1.txt");

  let buffer: Buffer | false;

  while ((buffer = input.next())) {
    lineFn(buffer.toString());
  }
};

export default readFileByLine;
