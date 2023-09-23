#!/usr/bin/python3
"""
Script that displays all values in the states table of hbtn_0e_0_usa
where the name matches the provided argument.
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

    # Execute the SQL query to retrieve states that match the provided name
    cursor.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC", (state_name,))

    # Fetch all the rows from the result set
    states = cursor.fetchall()

    # Print the results
    for state in states:
        print(state)

    # Close the cursor and the database connection
    cursor.close()
    db.close()

