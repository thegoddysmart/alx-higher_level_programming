#!/usr/bin/node
'use strict';

const fs = require('fs');
const path = process.argv[2];

if (!path) {
  console.error('Usage: ./readFile.js <file-path>');
  process.exit(1);
}

// Read the file content in utf-8 encoding
fs.readFile(path, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});

