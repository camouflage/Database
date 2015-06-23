#coding=utf-8
import MySQLdb
import SharedVar
from InfoInput import *
from Reservation import *
from CheckOut import *
from QueryEmptyRoom import *

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

