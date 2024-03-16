#!/usr/bin/python3
"""
retrive data "states" from hbtn_0e_0_usa"
TODO:
    1.  lists all cities from the database hbtn_0e_4_usa
    2.
    """


from sys import argv
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=argv[1],
                        passwd=argv[2],
                        db=argv[3],
                        charset="utf8"
                        )
    try:
        cur = conn.cursor()
        query = "SELECT cities.id, cities.name, states.name FROM cities \
                JOIN states ON cities.state_id=states.id \
                ORDER BY cities.id ASC"
        cur.execute(query)
        row = cur.fetchall()
        for r in row:
            print(r)
        cur.close()
        conn.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL database", str(e))
