#!/usr/bin/node

const { list } = require('./100-data');

function multiplyByIndex(value, index) {
  return value * index;
}

const newList = list.map(multiplyByIndex);

console.log(list);
console.log(newList);
