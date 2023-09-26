#!/usr/bin/python3
<<<<<<< HEAD
""" script that lists all State objects, and corresponding City objects, contained in the database hbtn_0e_101_usa
=======
""" prints the State object with the name passed as argument from the database
>>>>>>> 20bf18da5ed5abefc3a2141dfeeec21d84b3c6eb
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).order_by(State.id):
        print(instance.id, instance.name, sep=": ")
        for city_ins in instance.cities:
            print("    ", end="")
            print(city_ins.id, city_ins.name, sep=": ")
<<<<<<< HEAD

=======
>>>>>>> 20bf18da5ed5abefc3a2141dfeeec21d84b3c6eb
