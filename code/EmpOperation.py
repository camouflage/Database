#coding=utf-8
import MySQLdb
import SharedVar
from InfoInput import *

def EmpOp():
	"""
		Show Employees' operations.
	"""
	while 1:
		print "\nPlease enter the operation: "
		print "    0. logout"
		print "    1. InfoInput"
		print "    2. "

		op = input()
		if op == 0:
			return 0
		elif op == 1:
			InfoInput()
		elif op == 2:
			pass #To DO
		#elif op == 3:

		else:
			print "Wrong command!"

