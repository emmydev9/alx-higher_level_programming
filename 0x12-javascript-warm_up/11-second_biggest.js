#!/usr/bin/node

const len = process.argv.length;
const arr_ = [];

function compare (a, b) {
  return (a - b);
}

if (len < 4) {
  console.log(0);
} else {
  for (let i = 2; i < len; i++) {
    arr_.push(process.argv[i]);
  }
  console.log((arr_.sort(compare)[len - 4]));
}
