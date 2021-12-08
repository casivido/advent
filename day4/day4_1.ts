import { fileReader } from "../helpers/readfile";

const nextLine = fileReader("day4/input4.txt");

const numbers = (nextLine() || "")
  ?.split(",")
  .map((numStr) => parseInt(numStr));
nextLine();

let line: string | false;
let currentBingoCard: bingoCard = [];
const bingoCards: bingoCard[] = [];
while ((line = nextLine()) !== false) {
  if (line === "") {
    bingoCards.push(currentBingoCard);
    currentBingoCard = [];
    continue;
  }

  const lineNumbers = line
    .trim()
    .split(/\s+/)
    .map((numStr) => parseInt(numStr));
  currentBingoCard.push(lineNumbers);
}
bingoCards.push(currentBingoCard);

const numberLocations: Record<number, numberLocation[]> = {};
bingoCards.forEach((card, cardNumber) => {
  card.forEach((row, x) => {
    row.forEach((number, y) => {
      if (!numberLocations[number]) {
        numberLocations[number] = [];
      }

      numberLocations[number].push({ cardNumber, x, y });
    });
  });
});

const matches: Record<number, bingoMatches> = {};
const calledNumbers: Record<number, boolean> = {};
let matchedCard: number | false = false;
let numberIndex = 0;
let numberCalled = 0;
while (!matchedCard) {
  numberCalled = numbers[numberIndex++];

  calledNumbers[numberCalled] = true;
  const locations = numberLocations[numberCalled];
  if (locations) {
    locations.some((location) => {
      if (!matches[location.cardNumber]) {
        matches[location.cardNumber] = {
          horizontals: [0, 0, 0, 0, 0],
          verticals: [0, 0, 0, 0, 0],
          diagonals: [0, 0],
        };
      }

      matches[location.cardNumber].horizontals[location.y]++;
      matches[location.cardNumber].verticals[location.x]++;
      // if (location.x === location.y) {
      //   matches[location.cardNumber].diagonals[0]++;
      // }
      // if (location.x + location.y === 4) {
      //   matches[location.cardNumber].diagonals[1]++;
      // }

      if (
        Math.max(
          matches[location.cardNumber].horizontals[location.y],
          matches[location.cardNumber].verticals[location.x]
          // matches[location.cardNumber].diagonals[0],
          // matches[location.cardNumber].diagonals[1]
        ) === 5
      ) {
        matchedCard = location.cardNumber;
        return true;
      }
    });
  }
}

console.log(bingoCards[matchedCard]);
console.log(matchedCard);
console.log(numberCalled);

const sumUncalled = bingoCards[matchedCard].reduce(
  (acc, row) =>
    acc +
    row.reduce(
      (rowAcc, number) => rowAcc + (calledNumbers[number] ? 0 : number),
      0
    ),
  0
);
console.log(sumUncalled);
console.log(sumUncalled * numberCalled);

type bingoCard = number[][];
interface bingoMatches {
  horizontals: number[];
  verticals: number[];
  diagonals: number[];
}
interface numberLocation {
  cardNumber: number;
  x: number;
  y: number;
}
