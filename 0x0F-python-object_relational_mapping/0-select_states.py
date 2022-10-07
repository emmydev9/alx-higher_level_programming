#!/usr/bin/python3
""" list all states from a database """
import sys
import MySQLdb

if __name__ = "__main__":

	username = sys.argv[1]
	password = sys.argv[2]
	dbname = sys.argv[3]
	port = 3306

	db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=dbname, port=port)
	cur = db.cursor()
	cur.execute("SELECT * FROM states")
	states = cur.fetchall()

	for state in states:
		print(state)

