#coding=utf-8
import MySQLdb
import SharedVar
import datetime

def Reserve():
	"""
	Add reservation and update state of Room
	"""
	success = 0
	# while not success:
	print "\nAdd reservation:"
	EmpId = raw_input("Please input EmpId: ")
	GId = raw_input("Please input GId: ")
	RoomId = raw_input("Please input RoomId: ")
	startDate_string = raw_input("Please input startDate: ")
	endDate_string = raw_input("Please input endDate: ")
	

	#Deal with date strings
	startDate = datetime.datetime.strptime(startDate_string, "%Y-%m-%d")
	endDate = datetime.datetime.strptime(endDate_string, "%Y-%m-%d")

#<<<<<<< Updated upstream

	# NEED TO CHECK ROOM AVAILABILITY.

	#Query first
	db = MySQLdb.connect("127.0.0.1", "root", "", "test")
	cursor = db.cursor()
	sql = "SELECT * FROM Room WHERE RoomId = '%s' and available = 1" % RoomId
	cursor.execute(sql)
	data = cursor.fetchone()
	if data == None:
		print "This room is not available!"
		return

	db.close()


	# SQL operation
	db = MySQLdb.connect("127.0.0.1", "root", "", "test")
	cursor = db.cursor()
	sql = "INSERT INTO Reserve VALUES ('%s','%s','%s','%s','%s','%s')" % (EmpId,GId,RoomId,SharedVar.ResId,startDate,endDate)
	#print sql
	try:
		cursor.execute(sql)
		db.commit()
		print "Insert Reserve sucessfully!"
		success = 1
	except:
		print "Insert fail!"
		success = 0
		db.rollback();
		
	if success == 1:
		sql = "UPDATE Room SET available = 0 WHERE RoomId = '%s'" % (RoomId)
		try:
			cursor.execute(sql)
			db.commit()
# =======
# 		#SQL operation
# 		db = MySQLdb.connect("127.0.0.1", "root", "", "test")
# 		cursor = db.cursor()
# 		sql = "INSERT INTO Reserve VALUES ('%s','%s','%s','%s','%s','%s')" % (EmpId,GId,RoomId,SharedVar.ResId,startDate,endDate)
# 		#print sql
# 		try:
# 			cursor.execute(sql)
# 			db.commit()
# 			print "Insert Reserve sucessfully!"
# 		except:
# 			db.rollback();
# 			print "Insert fail!"

# 		sql = "UPDATE Room SET available = 0 WHERE RoomId = '%s'" % (RoomId)
# 		#print sql
# 		try:
# 			cursor.execute(sql)
# 			db.commit()
# 			print "update!"
# >>>>>>> Stashed changes
		except:
			db.rollback();
			success = 0
			print "Update available fail!"		

	db.close()

	if success == 1:
		SharedVar.ResId += 1

	SharedVar.commit()
