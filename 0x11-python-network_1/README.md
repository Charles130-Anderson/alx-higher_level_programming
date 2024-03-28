0x11. Python - Network #1
Resources
https://intranet.alxswe.com/rltoken/KoRrs5dVWsb-B82e-M1TQQ
https://intranet.alxswe.com/rltoken/OGcRGPr7TSWtzypDd0ZibQ
https://intranet.alxswe.com/rltoken/dUNaNQrV2bMSstILitQbXQ

To fetch internet resources with the Python package `urllib`, decode the response body, and make HTTP GET/POST/PUT requests, you can follow these steps:
### Fetching Internet Resources with urllib:

```python
import urllib.request

# Making a GET request
response = urllib.request.urlopen('https://example.com')
html = response.read().decode('utf-8')  # Decode response body
print(html)
```

### Using the Python package requests:

```python
import requests

# Making a GET request
response = requests.get('https://example.com')
print(response.text)  # Print response body

# Making a POST request
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('https://example.com/post', data=payload)
print(response.text)  # Print response body
```

### Fetching JSON resources:

```python
# Making a GET request for JSON
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
data = response.json()  # Automatically decodes JSON response
print(data)
```

### Manipulating Data from an External Service:

```python
# Example of manipulating data from an external service
for post in data:
    print("Title:", post['title'])
    print("Body:", post['body'])
    print("User ID:", post['userId'])
    print()
```
**Note:** Using `requests` is generally simpler and more user-friendly than `urllib`, as it provides a higher-level interface for making HTTP requests.

Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file at the root of the repo, containing a description of the repository
A README.md file, at the root of the folder of this project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
You must use get to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
Your code should not be executed when imported (by using if __name__ == "__main__":)

Tasks and solutions 
0. What's my status? #0
mandatory
Write a Python script that fetches https://alx-intranet.hbtn.io/status

You must use the package urllib
You are not allowed to import any packages other than urllib
The body of the response must be displayed like the following example (tabulation before -)
You must use a with statement
guillaume@ubuntu:~/0x11$ ./0-hbtn_status.py | cat -e
Body response:$
    - type: <class 'bytes'>$
    - content: b'OK'$
    - utf8 content: OK$
guillaume@ubuntu:~/0x11$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x11-python-network_1
File: 0-hbtn_status.py

Solution in Pseudocode 
1. Start
2. Define the URL to fetch as 'https://alx-intranet.hbtn.io/status'
3. Use the 'urllib.request.urlopen' function to open the URL
4. Use a 'with' statement to manage the connection and automatically close it when done
5. Inside the 'with' statement:
    6. Read the response body using the 'read' method
    7. Decode the response body from bytes to UTF-8 using the 'decode' method
    8. Print the header "Body response:"
    9. Print a tabulation and then "- type: " followed by the type of the response body
    10. Print a tabulation and then "- content: " followed by the content of the response body
    11. Print a tabulation and then "- utf8 content: " followed by the UTF-8 decoded content of the response body
12. End

1. Response header value #0
mandatory
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.

You must use the packages urllib and sys
You are not allow to import packages other than urllib and sys
The value of this variable is different for each request
You don’t need to check arguments passed to the script (number or type)
You must use a with statement
guillaume@ubuntu:~/0x11$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
ade2627e-41dd-4c34-b9d9-a0fa0f47b237
guillaume@ubuntu:~/0x11$ 
guillaume@ubuntu:~/0x11$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
6593e1f5-1b4b-4c9f-9c0e-72ab525b850f
guillaume@ubuntu:~/0x11$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x11-python-network_1
File: 1-hbtn_header.py

Solution 
1. Start
2. Define the URL as the command line argument passed to the script
3. Use the 'urllib.request.urlopen' function to open the URL
4. Use a 'with' statement to manage the connection and automatically close it when done
5. Inside the 'with' statement:
    6. Retrieve the value of the 'X-Request-Id' header from the response using the 'headers.get' method
    7. Print the value of the 'X-Request-Id' header
    8. End

2. POST an email #0
mandatory
Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)

The email must be sent in the email variable
You must use the packages urllib and sys
You are not allowed to import packages other than urllib and sys
You don’t need to check arguments passed to the script (number or type)
You must use the with statement
Please test your script in the sandbox provided, using the web server running on port 5000

guillaume@ubuntu:~/0x11$ ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
guillaume@ubuntu:~/0x11$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x11-python-network_1
File: 2-post_email.py

1. Start
2. Define the URL and email variables based on command-line arguments
3. Encode the email parameter
4. Open a connection to the URL using urllib.request.urlopen with a with statement
5. Send a POST request to the URL with the encoded email parameter
6. Retrieve and decode the response body
7. Print the decoded response body
8. End

3. Error code #0
mandatory
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).

You have to manage urllib.error.HTTPError exceptions and print: Error code: followed by the HTTP status code
You must use the packages urllib and sys
You are not allowed to import other packages than urllib and sys
You don’t need to check arguments passed to the script (number or type)
You must use the with statement
Please test your script in the sandbox provided, using the web server running on port 5000

guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000
Index
guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
guillaume@ubuntu:~/0x11$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x11-python-network_1
File: 3-error_code.py

sln1. Start
2. Define the URL variable based on command-line argument
3. Use a try-except block to handle potential HTTP errors
4. Inside the try block:
    5. Open a connection to the URL using urllib.request.urlopen with a with statement
    6. Read and decode the response body
    7. Print the decoded response body
8. Inside the except block for urllib.error.HTTPError:
    9. Print "Error code:" followed by the HTTP status code of the exception
10. End

4. What's my status? #1
mandatory
Write a Python script that fetches https://alx-intranet.hbtn.io/status

You must use the package requests
You are not allow to import packages other than requests
The body of the response must be display like the following example (tabulation before -)
guillaume@ubuntu:~/0x11$ ./4-hbtn_status.py | cat -e
Body response:$
    - type: <class 'str'>$
    - content: OK$
guillaume@ubuntu:~/0x11$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x11-python-network_1
File: 4-hbtn_status.py

soln
1. Start
2. Define the URL as 'https://alx-intranet.hbtn.io/status'
3. Send a GET request to the URL using requests.get()
4. Retrieve the response
5. Print the header "Body response:"
6. Print a tabulation and then "- type: " followed by the type of the response body
7. Print a tabulation and then "- content: " followed by the content of the response body
8. End

5. Response header value #1
mandatory
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header

You must use the packages requests and sys
You are not allow to import other packages than requests and sys
The value of this variable is different for each request
You don’t need to check script arguments (number and type)
guillaume@ubuntu:~/0x11$ ./5-hbtn_header.py https://alx-intranet.hbtn.io
5e52e160-c822-4669-8b3a-8b3bbca7b090
guillaume@ubuntu:~/0x11$ 
guillaume@ubuntu:~/0x11$ ./5-hbtn_header.py https://alx-intranet.hbtn.io
eaceaf35-bc0f-4f74-994a-7be0728ec654
guillaume@ubuntu:~/0x11$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x11-python-network_1
File: 5-hbtn_header.py

sln
1. Start
2. Define the URL based on the command-line argument
3. Send a GET request to the URL using requests.get()
4. Retrieve the response
5. Extract the value of the 'X-Request-Id' header from the response
6. Print the value of the 'X-Request-Id' header
7. End

6. POST an email #1
mandatory
Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.

The email must be sent in the variable email
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to error check arguments passed to the script (number or type)
Please test your script in the sandbox provided, using the web server running on port 5000

guillaume@ubuntu:~/0x11$ ./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
guillaume@ubuntu:~/0x11$ 

sln
1. Start
2. Define the URL and email address based on the command-line arguments
3. Define the data to be sent in the POST request with the email as a parameter
4. Send a POST request to the URL using requests.post()
5. Retrieve the response
6. Display the body of the response
7. End

7. Error code #1
mandatory
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.

If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
Please test your script in the sandbox provided, using the web server running on port 5000

guillaume@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000
Index
guillaume@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
guillaume@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
guillaume@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
guillaume@ubuntu:~/0x11$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x11-python-network_1
File: 7-error_code.py

sln
1. Start
2. Define the URL based on the command-line argument
3. Send a GET request to the URL using requests.get()
4. Retrieve the response
5. Check if the status code of the response is greater than or equal to 400
6. If the status code is greater than or equal to 400:
    7. Print "Error code:" followed by the value of the status code
8. Otherwise:
    9. Display the body of the response
10. End

8. Search API
mandatory
Write a Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.

The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and not empty, display the id and name like this: [<id>] <name>
Otherwise:
Display Not a valid JSON if the JSON is invalid
Display No result if the JSON is empty
You must use the package requests and sys
You are not allowed to import packages other than requests and sys
Please test your script in the sandbox provided, using the web server running on port 5000. All JSON generated by this server are random.

guillaume@ubuntu:~/0x11$ ./8-json_api.py 
No result
guillaume@ubuntu:~/0x11$ ./8-json_api.py a
[8446] amnirqhtfjq
guillaume@ubuntu:~/0x11$ ./8-json_api.py 2
No result
guillaume@ubuntu:~/0x11$ ./8-json_api.py b
[7094] bmofakakhke
guillaume@ubuntu:~/0x11$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x11-python-network_1
File: 8-json_api.py

sln
1. Start
2. Define the URL based on the command-line argument
3. If no argument is provided, set the value of 'q' to an empty string, else set it to the provided argument
4. Define the data to be sent in the POST request with the letter as a parameter
5. Send a POST request to the URL using requests.post()
6. Retrieve the response
7. Try to parse the response JSON
8. If JSON is successfully parsed:
    9. If the JSON is not empty:
        10. Display the id and name from the JSON response
    11. Otherwise:
        12. Print "No result"
9. If JSON parsing fails:
    10. Print "Not a valid JSON"
11. End

9. My GitHub!
mandatory
Write a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id

You must use Basic Authentication with a personal access token as password to access to your information (only read:user permission is needed)
The first argument will be your username
The second argument will be your password (in your case, a personal access token as password)
You must use the package requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
guillaume@ubuntu:~/0x11$ ./10-my_github.py papamuziko cisfun
2531536
guillaume@ubuntu:~/0x11$ ./10-my_github.py papamuziko wrong_pwd
None
guillaume@ubuntu:~/0x11$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x11-python-network_1
File: 10-my_github.py

sln 

1. Start
2. Get the GitHub username and password from the command-line arguments
3. Define the URL for the GitHub API to fetch user information
4. Send a GET request to the GitHub API with Basic Authentication using the provided username and password
5. Check if the request was successful (status code 200)
6. If the request was successful:
    7. Parse the response JSON to extract user information
    8. Display the user's id
7. If the request was not successful:
    8. Print None
9. End

#advanced
The Holberton School staff evaluates candidates applying for a back-end position with multiple technical challenges, like this one:

Please list 10 commits (from the most recent to oldest) of the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
Write a Python script that takes 2 arguments in order to solve this challenge.

The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
Only 17% of applicants for a backend position at Holberton finished this task in less than 15 minutes.

guillaume@ubuntu:~/0x11$ ./100-github_commits.py rails rails
3b5a6dfb18f33c373a89760c60d741f34206f23b: Jon Moss
f785ad786ae49dd6f7a2f1d77c44ea17008c6656: Jon Moss
bb13c37fefdc8b5699918b38eff84751c2899ad5: Rafael França
f5d880866917724217eae9785a3ccd3f806c5aaf: Rafael França
0da696a5e3cee87a996a020b664caa1eabd66220: Ryuta Kamizono
24eb450d7599bab1f5863e0578a21c65ca42a915: Matthew Draper
668f8691f1017042e238497d1a5b7b8bf1c43819: Matthew Draper
a76f5189f6cec4b3e6d9035e2b55dcda6050dfdb: Ryuta Kamizono
28079868d0e70bdac80c76cf806afd517edfe1e7: Rafael França
8f0d8551893789f26e5d6b82ccef00779296818f: Rafael Mendonça França
guillaume@ubuntu:~/0x11$ 
Be careful: only 60 requests by hour by IP for unauthenticated requests Rate limit

Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x11-python-network_1
File: 100-github_commits.py

sln

1. Start
2. Get the repository name and owner name from the command-line arguments
3. Define the URL for the GitHub API to fetch commits for the specified repository by the specified owner
4. Send a GET request to the GitHub API using requests.get()
5. Check if the request was successful (status code 200)
6. If the request was successful:
    7. Parse the response JSON to extract commits information
    8. Print the 10 most recent commits (from the most recent to oldest)
9. If the request was not successful:
    10. Print an error message with the response status code
11. End
