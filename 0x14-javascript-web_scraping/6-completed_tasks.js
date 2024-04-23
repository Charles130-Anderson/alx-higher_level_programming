#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, function (err, res, body) {
  if (err) {
    console.error('Error:', err);
    return;
  }

  if (res.statusCode !== 200) {
    console.error('Error:', 'An error occurred. Status code:', res.statusCode);
    return;
  }

  try {
    const tasks = JSON.parse(body);
    const completed = {};

    for (const task of tasks) {
      if (task.completed) {
        completed[task.userId] = (completed[task.userId] || 0) + 1;
      }
    }

    console.log(completed);
  } catch (parseErr) {
    console.error('Error parsing JSON:', parseErr);
  }
});
