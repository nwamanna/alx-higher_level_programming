#!/usr/bin/python3
""" This script lists all cities from the database hbtn_0e_4_usa """
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
    query = "SELECT c.id, c.name, s.name FROM cities c, states s\
             WHERE c.state_id = s.id ORDER BY c.id;"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
