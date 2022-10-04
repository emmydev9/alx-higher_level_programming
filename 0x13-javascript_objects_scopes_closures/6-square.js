#!/usr/bin/node

const Squares = require('./5-square.js');

class Square extends Squares {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let i = 0; i < this.size; i++) {
        let x = '';
        for (let j = 0; j < this.size; j++) {
          x += c;
        }
        console.log(x);
      }
    }
  }
}

module.exports = Square;
