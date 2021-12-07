import readlines from "n-readlines";

function readFileByLine<X>(
  filename: string,
  lineFn: (line: X) => void,
  transformFn: (buf: Buffer) => X
) {
  const input = new readlines(filename);

  let buffer: Buffer | false;
  while ((buffer = input.next())) {
    lineFn(transformFn(buffer));
  }
}

export default readFileByLine;
