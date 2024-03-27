# 0x10 Python - Network #0

## Introduction

Welcome to the 0x10 Python - Network #0 project! This project is part of the SE Foundations curriculum, aiming to enhance your understanding of Python, Bash scripting, and network concepts. The project is designed to be completed within a week, starting from March 27, 2024, and ending by March 28, 2024.

## Learning Objectives

By the end of this project, you should be able to:

- Understand and explain the basics of HTTP, including request methods, response status codes, and headers.
- Explain the structure of a URL, including the scheme, domain name, sub-domain, port number, and query string.
- Use cURL to make HTTP requests and understand the responses.
- Write Bash scripts to interact with web servers using cURL.
- Write Python scripts to solve problems related to network programming.

## Requirements

### General

- All scripts must be written using vi, vim, or emacs.
- The project must be completed on Ubuntu 20.04 LTS.
- Bash scripts must be exactly 3 lines long.
- Python scripts must be compatible with Python 3.8.5.
- All files must end with a new line.
- All files must be executable.
- Bash scripts must start with `#!/bin/bash` and include a comment explaining the script's purpose.
- Python scripts must start with `#!/usr/bin/python3`.
- Code must adhere to the pycodestyle (version 2.8.*).
- All modules, classes, and functions must be documented.

### Copyright and Plagiarism

- You are not allowed to copy and paste someone else's work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism will result in removal from the program.

## Tasks

### 0. cURL body size

Write a Bash script that takes a URL as input, sends a request to that URL using cURL, and displays the size of the response body in bytes.

### 1. cURL to the end

Write a Bash script that takes a URL as input, sends a GET request to the URL using cURL, and displays the body of the response.

### 2. cURL Method

Write a Bash script that sends a DELETE request to a URL passed as the first argument and displays the body of the response.

### 3. cURL only methods

Write a Bash script that takes a URL as input and displays all HTTP methods the server will accept.

### 4. cURL headers

Write a Bash script that takes a URL as input, sends a GET request to the URL using cURL, and displays the body of the response. The request must include a header variable `X-School-User-Id` with the value `98`.

### 5. cURL POST parameters

Write a Bash script that takes a URL as input, sends a POST request to the URL using cURL, and displays the body of the response. The request must include two variables: `email` with the value `test@gmail.com` and `subject` with the value `I will always be here for PLD`.

### 6. Find a peak

Write a Python function that finds a peak in a list of unsorted integers. The function must not import any modules and must have the lowest possible complexity.

### 7. Only status code

Write a Bash script that sends a request to a URL passed as an argument and displays only the status code of the response.

### 8. cURL a JSON file

Write a Bash script that sends a JSON POST request to a URL passed as the first argument and displays the body of the response. The request must include the contents of a file passed as the second argument.

### 9. Catch me if you can!

Write a Bash script that makes a request to `0.0.0.0:5000/catch_me` that causes the server to respond with a message containing `You got me!` in the body of the response.

## Resources

- Read or watch: HTTP (HyperText Transfer Protocol), HTTP Cookies.

## Submission

- The project will be checked automatically at the deadline.
- An auto-review will be launched at the deadline.

## Repository

- GitHub repository: [alx-higher_level_programming](https://github.com/alx-higher_level_programming)
- Directory: `0x10-python-network_0`

## Copyright

Copyright © 2024 ALX, All rights reserved.

Citations:
[1] https://www.drupal.org/docs/develop/managing-a-drupalorg-theme-module-or-distribution-project/documenting-your-project/readmemd-template
[2] https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/
[3] https://medium.com/analytics-vidhya/how-to-create-a-readme-md-file-8fb2e8ce24e3
[4] https://bulldogjob.com/readme/how-to-write-a-good-readme-for-your-github-project
[5] https://medium.com/@kc_clintone/the-ultimate-guide-to-writing-a-great-readme-md-for-your-project-3d49c2023357
[6] https://github.com/othneildrew/Best-README-Template
[7] https://codefellows.github.io/sea-python-401d6/assignments/project_04_readme.html
[8] https://www.geeksforgeeks.org/what-is-readme-md-file/
[9] https://www.youtube.com/watch?v=jeOfS90Flf8
