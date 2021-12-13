import { cloneDeep } from "lodash";
import readFileByLine from "../helpers/readfile";

interface Link {
  name: string;
  isBig: boolean;
}

const startLink = {
  name: "start",
  isBig: false,
};

const mapLinks: Record<string, Link[]> = {};
readFileByLine("day12/input12_1.txt", (line) => {
  const [linkA, linkB] = line.split("-");

  if (!mapLinks[linkA]) {
    mapLinks[linkA] = [];
  }
  if (!mapLinks[linkB]) {
    mapLinks[linkB] = [];
  }

  mapLinks[linkA].push({
    name: linkB,
    isBig: linkB.toUpperCase() === linkB,
  });
  mapLinks[linkB].push({
    name: linkA,
    isBig: linkA.toUpperCase() === linkA,
  });
});

let completePaths = 0;
const travelToLink = (
  link: Link,
  seenSmallTwice: boolean = false,
  seenNames: Record<string, boolean> = {}
) => {
  if (link.name === "end") {
    completePaths++;
    return;
  }

  if (!link.isBig && seenNames[link.name]) {
    if (seenSmallTwice || link.name === "start") {
      return;
    } else {
      seenSmallTwice = true;
    }
  }

  seenNames[link.name] = true;
  mapLinks[link.name].forEach((newLink) =>
    travelToLink(newLink, seenSmallTwice, cloneDeep(seenNames))
  );
};

travelToLink(startLink);
console.log(completePaths);
