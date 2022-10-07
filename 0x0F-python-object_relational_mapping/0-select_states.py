#!/usr/bin/python3
""" list all states from a database """
import sys
import MySQLdb

if __name__ == "__main__":

    u = sys.argv[1]
    p = sys.argv[2]
    db = sys.argv[3]
    port = 3306

    db = MySQLdb.connect(host="localhost", user=u, passwd=p, db=db, port=port)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    states = cur.fetchall()

    for state in states:
        print(state)
