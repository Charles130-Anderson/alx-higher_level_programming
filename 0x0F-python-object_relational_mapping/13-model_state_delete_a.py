#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter 'a'"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create engine to connect to MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query State objects with a name containing the letter 'a'
    states_to_delete_query = session.query(State)\
                                    .filter(State.name.like('%a%'))

    # Execute the query and retrieve all results
    states_to_delete = states_to_delete_query.all()

    # Delete the queried State objects
    for state in states_to_delete:
        session.delete(state)
    session.commit()

    # Close the session
    session.close()
