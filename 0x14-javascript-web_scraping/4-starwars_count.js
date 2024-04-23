#!/usr/bin/node

const newRequest = require('request');

newRequest(process.argv[2], function (err, res, body) {
  if (!err) {
    const results = JSON.parse(body).results;
    console.log(results.reduce((count, movie) => {
      return movie.characters.find((char) => char.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
