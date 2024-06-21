#!/usr/bin/python3
'''Creates a session that inputs data to a table
    Script fetches all the states
'''
import sys
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine) #sessions is what opens the session to input information
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
session.close()
