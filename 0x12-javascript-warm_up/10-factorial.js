#!/usr/bin/node

function factorial (n) {
  console.log(n);
}

const n = parseInt(process.argv[2]);

if (n) {
  console.log(factorial(n));
} else {
  console.log(1);
}
