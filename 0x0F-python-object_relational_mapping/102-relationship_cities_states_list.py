#!/usr/bin/python3
"""
Script that lists all City objects and their corresponding State objects
from the database hbtn_0e_101_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
from relationship_state import State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database),
                           pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database to get City objects and their linked State objects, sorted by cities.id
    query_result = session.query(City).order_by(City.id).all()

    # Loop through the results and display them as specified
    for city in query_result:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
