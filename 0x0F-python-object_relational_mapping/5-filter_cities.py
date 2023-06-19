#!/usr/bin/python3
""" This script takes in the name of a state as an argument and
    lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=args[1],
                         passwd=args[2],
                         db=args[3])
    cursor = db.cursor()
    query = "SELECT c.name FROM cities c WHERE c.state_id =\
                   (SELECT states.id FROM states WHERE states.name = %s)\
                   ORDER BY c.id;"
    cursor.execute(query, (args[4],))
    rows = cursor.fetchall()
    count = 0
    for row in rows:
        print(row[0], end="")
        if count < (len(rows) - 1):
            print(", ", end="")
        else:
            print()
        count += 1
    cursor.close()
