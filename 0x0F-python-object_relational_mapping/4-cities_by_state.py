#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa"""
import sys
import MySQLdb

if __name__ == '__main__':

	u = sys.argv[1]
	p = sys.argv[2]
	dbn = sys.argv[3]
	port = 3306

	db = MySQLdb.connect(host="localhost", user=u, passwd=p, db=dbn, port=port)
	cur = db.cursor()
	cur.execute("SELECT * FROM cities")
	cities = cur.fetchall()

	for city in cities:
		print(city)

