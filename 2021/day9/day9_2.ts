import _, { forEach, intersection, range } from "lodash";
import readFileByLine from "../helpers/readfile";

const map: number[][] = [];
readFileByLine("day9/input9_1.txt", (line: string) => {
  const newRow: number[] = [];
  line.split("").forEach((num) => newRow.push(parseInt(num)));
  map.push(newRow);
});

let X = 0;
let Y = 0;
const basinLayers: Record<number, BasinSpan[]> = {};
while (Y < map[0].length) {
  let curBasin: BasinSpan | undefined = undefined;

  while (X < map.length) {
    if (map[X][Y] === 9 && curBasin) {
      if (!basinLayers[Y]) {
        basinLayers[Y] = [];
      }
      curBasin.x2 = X - 1;
      basinLayers[Y].push(curBasin);
      curBasin = undefined;
    } else if (map[X][Y] !== 9) {
      if (!curBasin) {
        curBasin = {
          x1: X,
          x2: -1,
        };
      }
    }

    X++;
  }
  if (curBasin) {
    if (!basinLayers[Y]) {
      basinLayers[Y] = [];
    }
    curBasin.x2 = X - 1;
    basinLayers[Y].push(curBasin);
    curBasin = undefined;
  }

  X = 0;
  Y++;
}

let basins: Basin[] = [];

// Go thru each basin layer
forEach(basinLayers, (layer, yStr) => {
  const y: number = parseInt(yStr);
  // Go thru each basin span
  layer.forEach((basinSpan) => {
    // 1. Find previous connecting basins
    // 2. Combine into 1 basin
    // 3. Remove previous basins
    // 4. Add the comined basin
    const xRange = range(basinSpan.x1, basinSpan.x2 + 1);
    const curBasin: Basin = {
      locations: {
        [y]: [basinSpan],
      },
      value: xRange.length,
    };
    const connectingBasins: Basin[] = [curBasin];
    basins = basins.filter((prevBasin) => {
      const isConnected = prevBasin.locations[y - 1]?.some((prevLoc) => {
        const prevXRange = range(prevLoc.x1, prevLoc.x2 + 1);
        return intersection(xRange, prevXRange).length;
      });
      if (isConnected) {
        connectingBasins.push(prevBasin);
        return false;
      } else {
        return true;
      }
    });

    const starterLocations: Record<number, BasinSpan[]> = {};
    const combinedBasin = connectingBasins.reduce(
      (partialCombinedBasin, basin) => ({
        locations: range(0, y + 1).reduce((combinedLocations, y) => {
          combinedLocations[y] = (
            partialCombinedBasin.locations[y] || []
          ).concat(basin.locations[y] || []);
          return combinedLocations;
        }, starterLocations),
        value: partialCombinedBasin.value + basin.value,
      })
    );

    basins.push(combinedBasin);
  });
});

const basinValues = basins.map((basin) => basin.value);
basinValues.sort((a, b) => b - a);

const answer = basinValues[0] * basinValues[1] * basinValues[2];
console.log(answer);

interface BasinSpan {
  x1: number;
  x2: number;
}

interface Basin {
  locations: Record<number, BasinSpan[]>;
  value: number;
}
