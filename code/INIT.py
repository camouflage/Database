#coding=utf-8
import MySQLdb

def init():
	# connect to db.
	f = open("Global.sql")

	db = MySQLdb.connect("127.0.0.1", "root", "", "test")
	cursor = db.cursor()
	sql = f.read()
	cursor.execute(sql)
	db.close()

init()