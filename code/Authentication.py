#coding=utf-8
import MySQLdb
import getpass

def Authentication():
	"""
		Return: 0 for exit, 1 for Admin and 2 for Emp
	"""
	while 1:
		print "=                                         "
		print "=               请选择您的身份：              "
		print "=               0. exit					   "
		print "=               1. Administrator              "
		print "=               2. Employee                "
		op = input()
		if op == 0:
			return 0
		elif op == 1:
			if Authentication_Ad() == 1:
				return 1
		elif op == 2:
			if Authentication_Em() == 1:
				return 2
		else:
			print "Wrong command!"

def Authentication_Ad():
	"""
		Authentication for Administrator.
		Return: 1 for success, 0 for failure.
	"""
	UserId = raw_input("Enter your UserId: ")
	print "Enter your password: "
	password = getpass.getpass()
#	return 1 # For test, please rm

	db = MySQLdb.connect("127.0.0.1", "root", "", "test")
	cursor = db.cursor()
	sql = "select UserId from Administrator where UserId = '%s' and password = '%s'" %(UserId,password)
	print sql
	cursor.execute(sql)
	data = cursor.fetchone()
	#print data
	if ( data != None ):
		print "登陆成功!"
		return 1
	else:
		print "密码或用户名不正确，登录失败"
		return 0
	db.close()


def Authentication_Em():
	"""
		Authentication for Employee
		Return: 1 for success, 0 for failure.
	"""
	UserId = raw_input("Enter your UserId:")
	print "Enter your password:"
	password = getpass.getpass()
#	return 1 # For test, please rm

	db = MySQLdb.connect("127.0.0.1", "root", "", "test")
	cursor = db.cursor()
	sql = "select UserId from Employee where UserId = '%s' and password = '%s'" %(UserId,password)
	#print sql
	cursor.execute(sql)
	data = cursor.fetchone()
	if ( data != None ):
		print "登陆成功！"
		return 1
	else:
		print "密码或用户名不正确，登录失败"
		return 0
	db.close()

