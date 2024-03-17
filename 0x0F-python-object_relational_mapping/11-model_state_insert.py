#!/usr/bin/python3
"""script lists all State objects
add “Louisiana” to the database"
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
    add_state = State(name="Louisiana")
    session.add(add_state)
    session.commit()

    print('{0}'.format(add_state.id))
    session.close()
