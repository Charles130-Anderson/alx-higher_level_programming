#!/usr/bin/node

const newRequest = require('request');

newRequest.get(process.argv[2])
  .on('response', function (newResponse) {
    console.log(`code: ${newResponse.statusCode}`);
  });
