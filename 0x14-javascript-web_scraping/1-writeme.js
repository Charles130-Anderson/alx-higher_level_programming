#!/usr/bin/node

const newFs = require('fs');

newFs.writeFile(process.argv[2], process.argv[3], 'utf8', err => {
  if (err) {
    console.error(err);
  }
});
