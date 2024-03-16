#!/usr/bin/python3
"""
Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:

"""

from sys import argv
import MySQLdb


def main():
    connect = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=argv[1],
                        passwd=argv[2],
                        db=argv[3],
                        charset="utf8"
                            )
    cur = connect.cursor()
    query = "SELECT id, name FROM states WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC"
    cur.execute(query)
    f_query = cur.fetchall()
    for info in f_query:
        print(info)
    cur.close()
    connect.close()

if __name__ == "__main__":
    main()
