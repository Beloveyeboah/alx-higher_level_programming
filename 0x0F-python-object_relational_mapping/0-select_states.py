#!/usr/bin/python3

# a script that lists all states from the database hbtn_0e_0_usa:


from MySQLdb import _mysql

def list_states_mysql(username, password, database_name):
    """connect to mysql"""

    db = MySQLdb.connect(user = username, passwd = password, db = database_name, host = "localhost", port = 3306)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()

    if __name__ == "__main__":
        list_states_mysql("your_username", "your_password", "hbtn_0e_0_usa")
