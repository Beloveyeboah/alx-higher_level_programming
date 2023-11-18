#!/usr/bin/python3
"""
retrive data "states" from hbtn_0e_0_usa"
TODO:
    1. displays all values in the states
    2. where name matches the argument.
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
        search_state = argv[4]
        query = "SELECT * FROM states WHERE name = '{:s}' \
                ORDER BY id ASC".format(search_state)
        cur.execute(query)
        row = cur.fetchall()
        for r in row:
            if r[1] = search_state:
                print(r)
        cur.close()
        conn.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL database", str(e))
