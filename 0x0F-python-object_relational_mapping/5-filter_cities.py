#!/usr/bin/python3
"""
Script that lists all cities of that state, using the database hbtn_0e_4_usa
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
    query = """SELECT cities.name
               FROM cities
               JOIN states ON cities.state_id = states.id
               WHERE states.name = %s
               ORDER BY cities.id ASC"""

    # Execute query with parameterized input
    cursor.execute(query, (sys.argv[4],))

    # Fetch all results
    results = cursor.fetchall()

    # Print results
    cities = [row[0] for row in results]
    print(', '.join(cities))

    # Close cursor and connection
    cursor.close()
    db.close()
