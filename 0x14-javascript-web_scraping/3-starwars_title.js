#!/usr/bin/node

const newRequest = require('request');

const newUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

newRequest(newUrl, function (err, res, body) {
  console.log(err || JSON.parse(body).title);
});
