#!/usr/bin/python3
"""script lists all State objects
searches for the name of a given state
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    connects to the database
    """

    url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(url)
    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State).filter(State.name== argv[4]).first()
    if states:
        for state in states:
            print('{0}'.format(state.id))
    else:
        print('Not found')
