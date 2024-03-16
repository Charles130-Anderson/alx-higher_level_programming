#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument. (Safe from MySQL injection)
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")

    # Create cursor
    cursor = db.cursor()

    # Prepare the SQL query with parameterized input
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Execute query with parameterized input
    cursor.execute(query, (sys.argv[4],))

    # Fetch all results
    results = cursor.fetchall()

    # Print results
    for row in results:
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()
