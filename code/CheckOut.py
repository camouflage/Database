#coding=utf-8
import MySQLdb
import SharedVar
import datetime

def CheckOut():
	ResId_input = raw_input("Please input ResId: ")

	#Query first
	db = MySQLdb.connect("127.0.0.1", "root", "", "test")
	cursor = db.cursor()
	sql = "SELECT * FROM Reserve WHERE ResId = '%s'" % ResId_input
	print sql
#try:
	cursor.execute(sql)
	data = cursor.fetchone()


	EmpId = data[0]
	GId = data[1]
	RoomId = data[2]
	ResId = data[3]
	startDate = data[4]
	endDate = data[5]

	print "Reservation Information: "
	print "EmpId: "+EmpId+" GId: "+GId+" RoomId: "+RoomId+" ResId: "+ResId+" startDate: "+startDate.strftime("%Y-%m-%d")+" endDate: "+endDate.strftime("%Y-%m-%d")

#	    during = (endDate - startDate).days
	db.close()

	#Delete
	op = input("Are you sure to check out? \n0.No  1.Yes ")
	if op == 0:
		return
	elif op == 1:

		#Bill
		db = MySQLdb.connect("127.0.0.1", "root", "", "test")
		cursor = db.cursor()
		sql = "SELECT Room.price FROM Reserve,Room WHERE Reserve.RoomId = Room.RoomId AND Reserve.ResId = '%s'" % ResId_input
		print sql
		cursor.execute(sql)
		data = cursor.fetchone()

		price = data[0];
		total = price*(endDate-startDate).days
		print "Bill: "
		print total

		sql = "UPDATE Room SET available = 1 WHERE RoomId = '%s'" % (RoomId)
		print sql
		cursor.execute(sql)
		db.commit()

		db.close()
		Del(ResId)
	else:
		print "Error Command!"
#except:
#	print "No Reservation which ResId = " + ResId_input	

	return

def Del(ResId):
	db = MySQLdb.connect("127.0.0.1", "root", "", "test")
	cursor = db.cursor()
	sql = "DELETE FROM Reserve WHERE ResId = '%s'" % ResId
	print sql
	try:
		cursor.execute(sql)
		db.commit()
		print "Delete operation complete!"
	except:
		db.rollback() #rollback if error happens

	db.close()
	