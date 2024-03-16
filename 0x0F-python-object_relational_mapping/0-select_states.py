#!/usr/bin/python3

"""Write a script that lists all states from the database hbtn_0e_0_usa:

Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
"""

import MySQLdb
from sys import argv


connect = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3], charset="utf8")
cursor = connect.cursor()
query = cursor.execute("SELECT id, name FROM states ORDERD BY id ASC")
f_query = query.fetchall()
for info in f_query:
    print(info)

cursor.close()
connect.close()


if __name__ == "__main__":
    main()

