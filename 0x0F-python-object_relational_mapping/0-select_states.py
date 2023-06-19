#!/usr/bin/python3
""" This  script that lists all states from the database hbtn_0e_0_usa """
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
    cursor.execute("SELECT * FROM states ORDER BY  states.id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
