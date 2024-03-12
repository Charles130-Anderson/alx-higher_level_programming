#!/usr/bin/node

exports.esrever = function (list) {
  let reversed = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversed.pushi (list[i]);
  }
  return reversed;
};
