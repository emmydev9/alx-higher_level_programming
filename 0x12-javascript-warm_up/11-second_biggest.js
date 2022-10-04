#!/usr/bin/node

const len = process.argv.length;
const arr_ = [];

if (len < 4) {
  console.log(0);
} else {
  for (let i = 2; i < len; i++) {
    arr_.push(process.argv[i]);
  }
  console.log((arr_.sort()[len - 4]));
}
