#coding=utf-8
import MySQLdb
import getpass


def Authentication():
	print "=========================================="
	print "=         欢迎使用 HELEN 酒店管理系统         " 
	print "=                                         "
	print "=            made by the authors            "
	print "==========================================="

	while 1:
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
				return 1
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

"""
	db = MySQLdb.connect("127.0.0.1", "root", "", "test")
	cursor = db.cursor()
	sql = "select UserId from Administrator where UserId = " + UserId + " and password = "+ password
	#print sql
	cursor.execute(sql)
	data = cursor.fetchone()
	if ( data != null ):
		print "登陆成功!"
		return 1
	else:
		print "密码或用户名不正确，登录失败"
		return 0
	db.close()
"""

def Authentication_Em():
	"""
		Authentication for Employee
		Return: 1 for success, 0 for failure.
	"""
	UserId = raw_input("Enter your UserId:")
	print "Enter your password:"
	password = getpass.getpass()

"""
	db = MySQLdb.connect("127.0.0.1", "root", "", "test")
	cursor = db.cursor()
	sql = "select UserId from Employee where UserId = " + UserId + " and password = "+ password
	#print sql
	cursor.execute(sql)
	data = cursor.fetchone()
	if ( data != null ):
		print "登陆成功！"
	else:
		print "密码或用户名不正确，登录失败"
		return 0
	db.close()
"""

Authentication()