#!/usr/bin/node
const { readFile, writeFile } = require('fs');
const { args } = require('process');
const getCon = (file) => {
  return readFile(file, 'utf8');
};
const con= getCon(args[2]) + '' + getCont(args[3]);
writeFile(args[4], con, 'utf8', err => {
  if (err) throw err;
});
