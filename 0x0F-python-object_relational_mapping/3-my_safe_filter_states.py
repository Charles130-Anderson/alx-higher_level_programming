#!/usr/bin/python3
"""
Connect to MySQL, fetch states by name, and print.
"""

import MySQLdb
import sys


def main(user, password, db_name, state_name):
    """Connect to MySQL, fetch states by name, and print."""
    # Connect to the database
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db_name,
        charset="utf8"
    )
    cur = conn.cursor()

    # Use a parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))

    # Fetch and display the results
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    conn.close()
