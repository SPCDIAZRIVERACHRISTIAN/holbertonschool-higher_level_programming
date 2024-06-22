#!/usr/bin/python3

'''
    This is a script that changes the name
    of a State object from the database
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

    session = Session(engine)
    state_change = session.query(State).filter(State.id == 2).first()
    if state_change:
        state_change.name = 'New Mexico'
        session.commit()
