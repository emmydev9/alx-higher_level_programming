#!/usr/bin/node

exports.esrever = function (list) {
  for (let i = 0; i < list.length; i++) {
    for (let j = i + 1; j < list.length; j++) {
      const temp = list[i];
      list[i] = list[j];
      list[j] = temp;
    }
  }
  return list;
};
