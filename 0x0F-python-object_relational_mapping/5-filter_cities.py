#!/usr/bin/python3
"""
Script that lists all cities of a state from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the number of arguments is correct
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get the command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query with parameterized query to prevent SQL injection
    query = "SELECT GROUP_CONCAT(cities.name SEPARATOR ', ') FROM cities \
             INNER JOIN states ON cities.state_id = states.id \
             WHERE states.name = %s \
             ORDER BY cities.id ASC"
    cursor.execute(query, (state_name,))

    # Fetch the result from the query
    result = cursor.fetchone()

    if result and result[0]:
        print(result[0])

    # Close the cursor and the database connection
    cursor.close()
    db.close()

