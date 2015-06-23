#coding=utf-8
import MySQLdb
import SharedVar
import getpass

def AdminOp():
	"""
		Show Administrators' operations.
	"""
	while 1:
		print "\nPlease enter the operation category: "
		print "    0. logout"
		print "    1. Employee"
		print "    2. Room"
		# print "    3. Facility"
		op = input()
		if op == 0:
			return 0
		elif op == 1:
			Employee()
		elif op == 2:
			Room()
		# elif op == 3:
		# 	Facility()
		else:
			print "Wrong command!"

def Employee():
	"""
		Employee related operations.
	"""
	while 1:
		print "\nPlease enter the operation: "
		print "    0. return"
		print "    1. add employee"
		print "    2. reset employee password"
		print "    3. delete employee"
		op = input()

		if op == 0:
			return
		elif op == 1:
			#UserId = raw_input("Please input userId:")
			print "Please set password: "
			password = getpass.getpass()

			db = MySQLdb.connect("127.0.0.1", "root", "", "test")
			cursor = db.cursor()
			sql = "INSERT INTO Employee VALUES ('%s','%s')" % (SharedVar.UserId,password)
			# print sql
			try:
				cursor.execute(sql)
				db.commit()
				print "Add User %d successfully!" % (SharedVar.UserId)
				SharedVar.UserId += 1
			except:
				db.rollback()
			
			db.close()

			SharedVar.commit()
			return 
		elif op == 2:
			Uid = raw_input("Please enter the userId: ")
			print "Please set your new password: "
			password = getpass.getpass()

			db = MySQLdb.connect("127.0.0.1", "root", "", "test")
			cursor = db.cursor()
			sql = "UPDATE Employee SET password = '%s' where UserId = '%s'" % (password,Uid)
			# print sql

			try:
				cursor.execute(sql)
				db.commit()
				print "Reset password sucessfully!"
			except:
				print "Reset fail!"
				db.rollback()

			db.close()
			return
		elif op == 3:
			Uid = raw_input("Please enter the userId: ")

			#Query first
			db = MySQLdb.connect("127.0.0.1", "root", "", "test")
			cursor = db.cursor()
			sql = "SELECT * FROM Employee where UserId = '%s'" % (Uid)
			# print sql
			cursor.execute(sql)
			data = cursor.fetchone()
			if data == None:
				print "There is no userId = " + Uid
				db.close()
				return
			else:
				#Delete
				sql = "DELETE FROM Employee where UserId = '%s'" % (Uid)
				# print sql
				try:
					cursor.execute(sql)
					db.commit()
					print "Delete UserId = '%s' Completed!" % (Uid)
				except:
					print "Delete fail!"
					db.rollback()

			db.close()
			
			return
		else:
			print "Wrong command!"


def Room():
	"""
		Room related operations.
	"""
	while 1:
		print "\nPlease enter the operation: "
		print "    0. return"
		print "    1. add bigroom"
		print "    2. add singleroom"
		print "    3. add doubleroom"
		print "    4. change price"
		print "    5. delete room"
		op = input()

		if op == 0:
			return

		elif op == 1:
			price = input("Please input the price: ")
			BigFlag = 1
			DoubleFlag = 0
			SingleFlag = 0
			db = MySQLdb.connect("127.0.0.1", "root", "", "test")
			cursor = db.cursor()
			sql = "INSERT INTO Room VALUES ('%s', 1, '%d','%d','%d','%d')" % (SharedVar.RoomId,price,BigFlag,DoubleFlag,SingleFlag)
			# print sql
			try:
				cursor.execute(sql)
				db.commit()
				SharedVar.RoomId += 1
				print "Add bigroom successfully!"
			except:
				db.rollback()
				print "Add Fail!"
			
			db.close()	

			SharedVar.commit()
			return

		elif op == 2:
			price = input("Please input the price: ")
			BigFlag = 0
			DoubleFlag = 0
			SingleFlag = 1
			db = MySQLdb.connect("127.0.0.1", "root", "", "test")
			cursor = db.cursor()
			sql = "INSERT INTO Room VALUES ('%s', 1, '%d','%d','%d','%d')" % (SharedVar.RoomId,price,BigFlag,DoubleFlag,SingleFlag)
			# print sql
			try:
				cursor.execute(sql)
				db.commit()
				SharedVar.RoomId += 1
				print "Add singleroom successfully!"
			except:
				db.rollback()
				print "Add Fail!"
			
			db.close()

			SharedVar.commit()
			return

		elif op == 3:
			price = input("Please input the price: ")
			BigFlag = 0
			DoubleFlag = 1
			SingleFlag = 0
			db = MySQLdb.connect("127.0.0.1", "root", "", "test")
			cursor = db.cursor()
			sql = "INSERT INTO Room VALUES ('%s', 1, '%d','%d','%d','%d')" % (SharedVar.RoomId,price,BigFlag,DoubleFlag,SingleFlag)
			# print sql
			try:
				cursor.execute(sql)
				db.commit()
				SharedVar.RoomId += 1
				print "Add doubleroom successfully!"
			except:
				db.rollback()
				print "Add Fail!"
			
			db.close()
			
			SharedVar.commit()
			return

		elif op == 4:
			Rid = raw_input("Please enter the RoomId: ")
			#Query first
			db = MySQLdb.connect("127.0.0.1", "root", "", "test")
			cursor = db.cursor()
			sql = "SELECT * FROM Room where RoomId = '%s'" % (Rid)
			# print sql
			cursor.execute(sql)
			data = cursor.fetchone()
			if data == None:
				print "There is no RoomId = " + Rid
				db.close()
				return
			else:
				#update
				price = input("Please enter the new price: ")
				sql = "UPDATE Room SET price = '%d' WHERE RoomId = '%s'" % (price,Rid)
				# print sql
				try:
					cursor.execute(sql)
					db.commit()
					print "Change price successfully!"
				except:
					db.rollback()
					print "Change price fail!"

			db.close();
			return

		elif op == 5:
			Rid = raw_input("Please enter the RoomId: ")
			#Query first
			db = MySQLdb.connect("127.0.0.1", "root", "", "test")
			cursor = db.cursor()
			sql = "SELECT * FROM Room where RoomId = '%s'" % (Rid)
			# print sql
			cursor.execute(sql)
			data = cursor.fetchone()
			if data == None:
				print "There is no RoomId = " + Rid
				db.close()
				return
			else:
				#delete
				sql = "DELETE FROM Room where RoomId = '%s'" % (Rid)
				# print sql
				try:
					cursor.execute(sql)
					db.commit()
					print "Delete RoomId = '%s' Completed!" % (Rid)
				except:
					print "Delete fail!"
					db.rollback()

			db.close()
			return

		else:
			print "Wrong command!"

"""
def Facility():
	while 1:
		print "\nPlease enter the operation: "
		print "    0. return"
		print "    1. add gym"
		print "    2. add chessroom"
		op = input()

		if op == 0:
			return

		elif op == 1:
			type = raw_input("Please enter the type: ")
			SharedVar.FacilityId += 1
			return 

		elif op == 2:
			size = raw_input("Please enter the size: ")
			SharedVar.FacilityId += 1
			return

		else:
			print "Wrong command!"
"""
