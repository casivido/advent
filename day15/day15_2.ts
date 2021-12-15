import readFileByLine from "../helpers/readfile";
import Graph from "node-dijkstra";
import { range } from "lodash";

const map = new Graph();

const nodes: number[][] = [];
readFileByLine("day15/input15_1.txt", (line) => {
  const riskLine = line.split("").map((str) => parseInt(str));
  let combinedRisks = [...riskLine];
  range(1, 5).forEach((i) => {
    combinedRisks = combinedRisks.concat(
      riskLine.map((risk) => {
        const newRisk = risk + i;
        return newRisk > 9 ? newRisk - 9 : newRisk;
      })
    );
  });
  nodes.push(combinedRisks);
});

const baseXLength = nodes.length;
const baseYLength = nodes[0].length;
range(1, 5).forEach((i) => {
  range(0, baseXLength).forEach((x) => {
    nodes.push(
      nodes[x].map((risk) => {
        const newRisk = risk + i;
        return newRisk > 9 ? newRisk - 9 : newRisk;
      })
    );
  });
});

const maxX = nodes.length - 1;
const maxY = nodes[0].length - 1;
range(0, maxX + 1).forEach((x) => {
  range(0, maxY + 1).forEach((y) => {
    const node = `${x}-${y}`;
    const targetNodes: Record<string, number> = {};
    [
      [x, y + 1],
      [x, y - 1],
      [x + 1, y],
      [x - 1, y],
    ].forEach(([curX, curY]) => {
      if (curX > maxX || curY > maxY || curX < 0 || curY < 0) {
        return;
      }

      const curNode = `${curX}-${curY}`;

      targetNodes[curNode] = nodes[curX][curY];
    });

    map.addNode(node, targetNodes);
  });
});

console.log(map.path("0-0", `${maxX}-${maxY}`, { cost: true }));

// route.addNode("A", { B: 1 });
// route.addNode("B", { A: 1, C: 2, D: 4 });
// route.addNode("C", { B: 2, D: 1 });
// route.addNode("D", { C: 1, B: 4 });

// route.path("A", "D");
