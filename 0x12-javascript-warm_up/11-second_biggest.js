#!/usr/bin/node
const args = process.argv.length;
if (args <= 3) {
  console.log(0);
} else {
  const arry = process.argv.slice(2).map(Number);
  const sArr = arry.sort(function (a, b) { return b - a; })[1];
  console.log(sArr);
}
