#!/usr/bin/node
const fs = require('fs');

const first_arg = fs.readFileSync(process.argv[2]).toString();
const second_arg = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], first_arg + second_arg);
