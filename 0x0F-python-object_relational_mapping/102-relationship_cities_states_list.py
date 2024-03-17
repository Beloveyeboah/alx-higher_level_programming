#!/usr/bin/python3
""" lists all City objects from the database hbtn_0e_101_usa
from the database `hbtn_0e_14_usa`.
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    connects to the database and get the cities
    from the database.
    """

    uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(uri)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    st_query = session.query(State).join(City).order_by(City.id).all()
    for state in st_query:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
