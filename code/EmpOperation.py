#coding=utf-8
import MySQLdb
import SharedVar
from InfoInput import *
from Reservation import *
from CheckOut import *

def EmpOp():
	"""
		Show Employees' operations.
	"""
	while 1:
		print "\nPlease enter the operation: "
		print "    0. logout"
		print "    1. InfoInput"
		print "    2. QueryEmptyRoom"
		print "    3. Reserve"
		print "    4. Check out"

		op = input()
		if op == 0:
			return 0
		elif op == 1:
			InfoInput()
		elif op == 2:
			QueryEmptyRoom()
		elif op == 3:
			Reserve()
		elif op == 4:
			CheckOut()
		else:
			print "Wrong command!"


def QueryEmptyRoom():
	"""
	Do query for empty room,
	return the first room which match the type of the room requested
	"""
	while 1:
		print "\nPlease enter the room type you want: "
		print "    0. exit"
		print "    1. BigRoom"
		print "    2. DoubleRoom"
		print "    3. SingleRoom"

		roomType = input()
		if roomType == 0:
			return 0
#	    if roomType != 1 && roomType != 2 && roomType != 3:
#	    	print "Wrong command!"

	   	elif roomType == 1: #BigRoom type
			db = MySQLdb.connect("127.0.0.1", "root", "", "test")
			cursor = db.cursor()
			sql = "SELECT RoomId FROM Room WHERE BigFlag = 1 AND available = 0"
			print sql
			cursor.execute(sql)
			data = cursor.fetchone()
			roomId = data[0]
			#print data
			print "Available room: " + roomId
			db.close()


		elif roomType == 2: #DoubleRoom type
			db = MySQLdb.connect("127.0.0.1", "root", "", "test")
			cursor = db.cursor()
			sql = "SELECT RoomId FROM Room WHERE DoubleFlag = 1 AND available = 0"
			print sql
			cursor.execute(sql)
			data = cursor.fetchone()
			roomId = data[0]
			#print data
			print "Available room: " + roomId
			print "Available room: '%s'" % (data)
			db.close()

		elif roomType == 3: #DoubleRoom type
			db = MySQLdb.connect("127.0.0.1", "root", "", "test")
			cursor = db.cursor()
			sql = "SELECT RoomId FROM Room WHERE SingleFlag = 1 AND available = 0"
			print sql
			cursor.execute(sql)
			data = cursor.fetchone()
			roomId = data[0]
			#print data
			print "Available room: " + roomId
			db.close()
		else:
			print "Wrong command "

