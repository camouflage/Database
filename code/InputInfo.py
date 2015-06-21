#coding=utf-8
import MySQLdb

def InputInfo():
	"""
		For Employee, get the info of Guest and store it.
		Return: 1 for completing input and 0 for not completing.
	"""
	while 1:
		guestType = input("\nPlease enter the guestType:\
			\n0. return\n1. Person\n2. Company\n")

		global GId
		if guestType == 0:
			return

		elif guestType == 1:
			Ssn = raw_input("Please enter Ssn: ")
			age = raw_input("Please enter age: ")
			gender = raw_input("Please enter gender: ")
			firstName = raw_input("Please enter firstName: ")
			lastName = raw_input("Please enter lastName: ")

			VIP = raw_input("is VIP(0. N0  1. Yes)? ")
			if VIP == 1:
				Vid = raw_input("Please enter Vid: ")
				status = raw_input("Please enter VIP Status: ")


			GId += 1
			return

		elif guestType == 2:
			cName = raw_input("Please enter company name: ")
			cAddress = raw_input("Please enter company address: ")


			GId += 1
			return

		else:
			print "Wrong command!"

GId = 0
InputInfo()
print GId