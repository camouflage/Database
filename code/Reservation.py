#coding=utf-8
import MySQLdb
import SharedVar
import datetime

def Reserve():
	"""
	Add reservation and update state of Room
	"""
	while 1:
		print "\nAdd reservation:"
		EmpId = raw_input("Please input EmpId: ")
		GId = raw_input("Please input GId: ")
		RoomId = raw_input("Please input RoomId: ")
		SharedVar.ResId += 1
		startDate_string = raw_input("Please input startDate: ")
		endDate_string = raw_input("Please input endDate: ")
		

		#Deal with date strings
		startDate = datetime.datetime.strptime(startDate_string, "%Y-%m-%d")
		endDate = datetime.datetime.strptime(endDate_string, "%Y-%m-%d")

		#SQL operation
		db = MySQLdb.connect("127.0.0.1", "root", "", "test")
		cursor = db.cursor()
		sql = "INSERT INTO Reserve VALUES ('%s','%s','%s','%s','%s','%s')" % (EmpId,GId,RoomId,SharedVar.ResId,startDate,endDate)
		print sql
		try:
			cursor.execute(sql)
			db.commit()
			print "Insert Reserve sucessfully!"
			break
		except:
			db.rollback();
			print "Insert fail!"

	db.close()

	SharedVar.commit()
