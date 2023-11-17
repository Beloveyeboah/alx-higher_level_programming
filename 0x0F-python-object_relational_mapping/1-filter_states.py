#!/usr/bin/python3
"""
retrive data "states" from hbtn_0e_0_usa"
TODO:
    1. print from state
    2. name starting with N (upper N)
    """


from sys import argv
import MySQLdb


def main():
    conn = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=argv[1],
                        passwd=argv[2],
                        db=argv[3],
                        charset="utf8"
                            )
    cur = conn.cursor()
    query = "SELECT id,name FROM states WHERE name  LIKE 'N%' ORDER BY id ASC"
    cur.execute(query)
    row = cur.fetchall()
    for r in row:
        print(r)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
