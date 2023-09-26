#!/usr/bin/python3
<<<<<<< HEAD
"""  script that lists all states from the database hbtn_0e_0_usa """
=======
"""  lists all states from the database hbtn_0e_0_usa """
>>>>>>> 20bf18da5ed5abefc3a2141dfeeec21d84b3c6eb
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
<<<<<<< HEAD

=======
>>>>>>> 20bf18da5ed5abefc3a2141dfeeec21d84b3c6eb
