#!/usr/bin/node

const process = require('process');
const fs = require('fs');

const filename = process.argv[2];
const data = process.argv[3];
fs.writeFile(filename, data, 'utf8', function (err) {
  if (err) {
    return err;
  }
  return data > filename;
});
