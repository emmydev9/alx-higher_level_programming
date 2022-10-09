#!/usr/bin/python3
""" search a states from a database in a safe way"""
import sys
import MySQLdb


if __name__ == "__main__":
    u = sys.argv[1]
    p = sys.argv[2]
    db = sys.argv[3]
    search = sys.argv[4]
    port = 3306

    db = MySQLdb.connect(host="localhost", user=u, passwd=p, db=db, port=port)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s;", (search,))
    states = cur.fetchall()

    for state in states:
        print(state)
