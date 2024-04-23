#!/usr/bin/node

const newFs = require('fs');
const newRequest = require('request');

newRequest(process.argv[2]).pipe(newFs.createWriteStream(process.argv[3]));
