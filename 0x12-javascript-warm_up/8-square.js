#!/usr/bin/node

if (parseInt(process.argv[2])) {
  const size = parseInt(process.argv[2]);
  for (let i = 0; i < size; i++) {
    let s = '';
    for (let j = 0; j < size; j++) {
      s += 'X';
    }
    console.log(s);
  }
} else {
  console.log('Missing size');
}
