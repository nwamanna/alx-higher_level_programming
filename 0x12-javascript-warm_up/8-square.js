#!/usr/bin/node
const args = process.argv;
const num = parseInt(args[2], 10);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    const output = 'X'.repeat(num);
    console.log(output);
  }
}
