#!/usr/bin/python3

# a script that lists all states from the database hbtn_0e_0_usa:


import MySQLdb
from sys import argv


if __name__ == "__main__":
    """retrive data of states from the db"""

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    _cursor = db.cursor()

    _cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = _cursor.fetchall()
    for row in rows:
        print(row)
    _cursor.close()
