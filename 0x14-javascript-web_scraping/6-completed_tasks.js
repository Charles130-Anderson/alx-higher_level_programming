#!/usr/bin/node

const newRequest = require('request');

const newApiUrl = process.argv[2];

newRequest(newApiUrl, function (err, res, body) {
  if (err) {
    console.error('Error:', err);
    return;
  }

  if (res.statusCode !== 200) {
    console.error('Error:', 'Unexpected status code:', res.statusCode);
    return;
  }

  try {
    const todos = JSON.parse(body);

    const completed = {};

    todos.forEach((todo) => {
      if (todo.completed) {
        if (completed[todo.userId] === undefined) {
          completed[todo.userId] = 1;
        } else {
          completed[todo.userId]++;
        }
      }
    });

    const output = `{${Object.entries(completed).map(([key, value]) => ` '${key}': ${value}`).join(',\n ')} }`;

    console.log(Object.keys(completed).length > 2 ? output : completed);
  } catch (parseErr) {
    console.error('Error parsing JSON:', parseErr);
  }
});
