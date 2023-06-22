#!/usr/bin/python3
""" This script takes in an argument and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument
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
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                   .format(args[4]))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
