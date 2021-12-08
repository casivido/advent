import { read } from "fs";
import readlines from "n-readlines";

function getInputStream(filename: string) {
  return new readlines(filename);
}

function readFileByLine(filename: string, lineFn: (line: string) => void) {
  const input = getInputStream(filename);

  let buffer: Buffer | false;
  while ((buffer = input.next())) {
    lineFn(buffer.toString());
  }
}

export function fileReader(filename: string) {
  const input = getInputStream(filename);

  return () => {
    const buffer = input.next();
    return buffer ? buffer.toString() : false;
  };
}

export default readFileByLine;
