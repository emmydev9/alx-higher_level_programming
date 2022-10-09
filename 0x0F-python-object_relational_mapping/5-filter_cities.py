#!/usr/bin/python3
"""lists all cities of that state"""
import sys
import MySQLdb

if __name__ == '__main__':

    u = sys.argv[1]
    p = sys.argv[2]
    dbn = sys.argv[3]
    state = sys.argv[4]
    port = 3306

    db = MySQLdb.connect(host="localhost", user=p, passwd=p, db=dbn, port=port)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
        FROM cities JOIN states ON cities.state_id = states.id \
        where states.name = %s", (state,))
    states = cur.fetchall()

    print(", ".join(state[1] for state in states))
