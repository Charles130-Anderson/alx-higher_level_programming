#!/usr/bin/python3
"""
Lists 10 commits of a repository by a specific user.
"""

import requests
import sys

if __name__ == "__main__":
    repository = sys.argv[1]
    owner = sys.argv[2]

    # Define the URL for the GitHub API to fetch commits
    url = f"https://api.github.com/repos/{owner}/{repository}/commits"

    # Send a GET request to the GitHub API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        commits = response.json()

        # Print the 10 most recent commits
        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print("Error:", response.status_code)
