#!/usr/bin/python3
""" script that prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    table = session.query(City, State).filter(
                                              City.state_id == State.id
                                             ).order_by(City.id)
    for c, s in table:
        print('{}: ({}) {}'.format(s.name, c.id, c.name))
