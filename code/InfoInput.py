#coding=utf-8
import MySQLdb
import SharedVar

def InfoInput():
	"""
		For Employee, get the info of Guest and store it.
		Return: 1 for completing input and 0 for not completing.
	"""
	while 1:
		guestType = input("\nPlease enter the guestType:\
			\n0. return\n1. Person\n2. Company\n")

		if guestType == 0:
			return

		elif guestType == 1:
			# Basic info
			SSN = raw_input("Please enter Ssn: ")
			age = raw_input("Please enter age: ")
			gender = raw_input("Please enter gender: ")
			firstName = raw_input("Please enter firstName: ")
			lastName = raw_input("Please enter lastName: ")

			db = MySQLdb.connect("127.0.0.1", "root", "", "test")
			cursor = db.cursor()
			sql = "INSERT INTO Person VALUES ('%s','%s','%s','%s','%s','%s')" % (SSN,age,gender,firstName,lastName,SharedVar.GId)
			print sql
			try:
				cursor.execute(sql)
				db.commit()
				print "Add Person complete!"
			except:
				db.rollback()
			db.close()
			# VIP
			VIP = input("Is VIP(0. N0  1. Yes)? ")
			if VIP == 1:
				Vid = raw_input("Please enter Vid: ")
				status = raw_input("Please enter VIP Status: ")

				db = MySQLdb.connect("127.0.0.1", "root", "", "test")
				cursor = db.cursor()
				sql = "INSERT INTO Guest VALUES ('%s','VIP','%s')" % (SharedVar.GId,Vid)
				print sql
				try:
					cursor.execute(sql)
					db.commit()
					print "Add VIP complete!"
				except:
					db.rollback()
				db.close()
			else:
				db = MySQLdb.connect("127.0.0.1", "root", "", "test")
				cursor = db.cursor()
				sql = "INSERT INTO Guest VALUES ('%s','Ordinary')" % (SharedVar.GId)
				print sql
				try:
					cursor.execute(sql)
					db.commit()
					print "Add Guest complete!"
				except:
					db.rollback()
				db.close()


			# Contacts
			tel = []
			while 1:
				no = raw_input("Please enter telephone number: ")
				tel.append(no)
				more = input("More contact infomation(0. N0  1. Yes)? ")
				if more != 1:
					break

			SharedVar.GId += 1

			db = MySQLdb.connect("127.0.0.1", "root", "", "test")
			cursor = db.cursor()
			for a in tel:
				sql = "INSERT INTO Contact VALUES ('%s','%s')" % (SharedVar.GId,a)
				print sql
				try:
					cursor.execute(sql)
					db.commit()
					print "Add Contact complete!"
				except:
					db.rollback()
		
			db.close()

			SharedVar.commit()
			return

		elif guestType == 2:
			# Basic info
			cName = raw_input("Please enter company name: ")
			cAddress = raw_input("Please enter company address: ")

			# Contacts
			tel = []
			while 1:
				no = raw_input("Please enter telephone number: ")
				tel.append(no)
				more = input("More contact infomation(0. N0  1. Yes)? ")
				if more != 1:
					break

			SharedVar.GId += 1

			db = MySQLdb.connect("127.0.0.1", "root", "", "test")
			cursor = db.cursor()
			sql = "INSERT INTO Company VALUES ('%s','%s','%s')" % (cName,cAddress,SharedVar.GId)
			print sql
			try:
				cursor.execute(sql)
				db.commit()
				print "Add Company complete!"
			except:
				db.rollback()

			for a in tel:
				sql = "INSERT INTO Contact VALUES ('%s','%s')" % (SharedVar.GId,a)
				print sql
				try:
					cursor.execute(sql)
					db.commit()
					print "Add Contact complete!"
				except:
					db.rollback()

			db.close()

			SharedVar.commit()
			return

		else:
			print "Wrong command!"
