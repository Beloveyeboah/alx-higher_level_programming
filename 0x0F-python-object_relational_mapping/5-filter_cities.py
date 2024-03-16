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
        state_arg = argv[4]
        cur = conn.cursor()
        query = "SELECT cities.name FROM cities \
                JOIN states ON cities.state_id=states.id \
                WHERE states.name LIKE %s \
                ORDER BY cities.id ASC"
        cur.execute(query, (state_arg,))
        row = cur.fetchall()
        if row is not None:
            print(", ".join([r[0] for r in row]))
        cur.close()
        conn.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL database", str(e))
