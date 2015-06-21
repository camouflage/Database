#coding=utf-8
import MySQLdb

def SelectOp():
	"""
		Show Administrators' operations.
	"""
	while 1:
		print "\nPlease enter the operation category: "
		print "    0. logout"
		print "    1. Employee"
		print "    2. Room"
		print "    3. Facility"
		op = input()
		if op == 0:
			return 0
		elif op == 1:
			Employee()
		elif op == 2:
			Room()
		elif op == 3:
			Facility()
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

		global UserId
		if op == 0:
			return
		elif op == 1:
			UserId += 1
			return 
		elif op == 2:
			Uid = raw_input("Please enter the userId: ")
			return
		elif op == 3:
			Uid = raw_input("Please enter the userId: ")
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

		global RoomId
		if op == 0:
			return

		elif op == 1:
			RoomId += 1
			return 

		elif op == 2:
			RoomId += 1
			return

		elif op == 3:
			RoomId += 1
			return

		elif op == 4:
			Rid = raw_input("Please enter the RoomId: ")
			return

		elif op == 5:
			Rid = raw_input("Please enter the RoomId: ")
			return

		else:
			print "Wrong command!"


def Facility():
	"""
		Facility related operations.
	"""
	while 1:
		print "\nPlease enter the operation: "
		print "    0. return"
		print "    1. add gym"
		print "    2. add chessroom"
		op = input()

		global FacilityId
		if op == 0:
			return

		elif op == 1:
			FacilityId += 1
			return 

		elif op == 2:
			FacilityId += 1
			return

		else:
			print "Wrong command!"

UserId = 0
RoomId = 0
FacilityId = 0
SelectOp()
