#!/usr/bin/node
const dict = require('./101-data').dict;
const dictKeys = Object.keys(dict);
const dictValues = Object.values(dict);
let matched;
const result = {};
// loop over the values
for (let i = 0; i < dictValues.length; i++) {
  result[JSON.stringify(dictValues[i])] = [];
  matched = dictKeys.filter(key => dict[key] === dictValues[i]);
  matched.forEach(item => result[JSON.stringify(dictValues[i])].push(item));
}
console.log(result);
