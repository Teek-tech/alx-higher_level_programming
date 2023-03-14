#!/usr/bin/node

/*
Tough algorithim I've written,
with a time Complexity of O(n)
*/
exports.esrever = function (list) {
  const listLen = list.length;
  const newList = [];

  for (let i = listLen; i >= 0; i--) {
    newList.push(list[i]);
  }
  return (newList.slice(1, newList.length));
};
