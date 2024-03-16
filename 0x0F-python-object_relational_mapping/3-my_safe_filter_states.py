#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument. (Safe from MySQL injection)
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    # Create cursor
    cursor = db.cursor()

    # Execute query with parameterized input
    match = sys.argv[4]  # Store the search term
    cursor.execute("SELECT * FROM states WHERE name LIKE %s", (match,))

    # Fetch all results
    results = cursor.fetchall()

    # Print results
    for row in results:
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()
