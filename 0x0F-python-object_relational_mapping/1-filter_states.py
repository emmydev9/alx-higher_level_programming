#!/usr/bin/python3
"""lists all states with a name starting
with N (upper N) from the database"""
import sys
import MySQLdb

if __name__ == "__main__":
    u = sys.argv[1]
    p = sys.argv[2]
    dbn = sys.argv[3]
    port = 3306

    db = MySQLdb.connect(host="localhost", user=u, passwd=p, db=dbn, port=port)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE\
        CONVERT(`name` USING Latin1)\
     COLLATE Latin1_General_CS LIKE 'N%';")
    states = cur.fetchall()

    for state in states:
        print(state)
