#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    # Create cursor
    cursor = db.cursor()

    # Execute the SQL query
    cursor.execute = """SELECT cities.id, cities.name, states.name
               FROM cities
               INNER JOIN states ON cities.state_id = states.id
               ORDER BY cities.id ASC"""

    # Fetch all results
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()
