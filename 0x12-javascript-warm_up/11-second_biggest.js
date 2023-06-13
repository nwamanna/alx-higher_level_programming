#!/usr/bin/node
const args = process.argv.length;
if (args === 3) {
  console.log(0);
} else if (args > 3) {
  console.log('Arguments found');
} else {
  console.log(0);
}
