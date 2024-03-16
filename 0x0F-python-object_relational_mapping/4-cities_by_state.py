#!/usr/bin/python3
"""
Write a script that lists all cities from the database hbtn_0e_4_usa

TODO:
    Results must be sorted in ascending order by cities.id
    """

if __name__ == "__main__":
    connection = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=argv[1],
                        passwd=argv[2],
                        db=argv[3],
                        charset="utf8"
                        )
    try:
        cur = connection.cursor()
        query = "SELECT cities.id, cities.name, states.name FROM cities \
                JOIN states ON cities.state_id=states.id \
                ORDER BY cities.id ASC"
        cur.execute(query)
        for r in row:
            print(r)
        cur.close()
        connection.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL database", str(e))
