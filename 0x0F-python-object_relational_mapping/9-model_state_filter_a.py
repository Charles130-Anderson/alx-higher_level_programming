#!/usr/bin/python3
"""Lists all State objects that contain the letter 'a' from the database"""

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

    # Query all State objects containing the letter 'a'
    states_with_a = session.query(State)\
                           .filter(State.name.like('%a%'))\
                           .order_by(State.id)\
                           .all()

    # Print results
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
