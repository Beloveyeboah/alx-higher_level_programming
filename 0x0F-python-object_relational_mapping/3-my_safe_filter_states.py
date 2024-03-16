#!/usr/bin/python3
"""
. SQL Injection...
TODO:
    1. write one that is safe from MySQL injections!
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
        search_state = argv[4]
        query = "SELECT * FROM states WHERE name = %s \
                ORDER BY id ASC"
        cur.execute(query, (search_state,))
        row = cur.fetchall()
        for r in row:
            if r[1] == search_state:
                print(r)
        cur.close()
        conn.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL database", str(e))
