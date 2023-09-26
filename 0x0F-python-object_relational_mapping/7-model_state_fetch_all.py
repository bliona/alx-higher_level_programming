#!/usr/bin/python3
<<<<<<< HEAD
"""script that lists all State objects from the database hbtn_0e_6_usa
=======
"""Start link class to table in database
>>>>>>> 20bf18da5ed5abefc3a2141dfeeec21d84b3c6eb
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).order_by(State.id):
        print(instance.id, instance.name, sep=": ")
