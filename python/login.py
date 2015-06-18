#coding=utf-8
import MySQLdb

def Login():
	print "=========================================="
	print "=         欢迎使用 HELEN 酒店管理系统         " 
	print "=                                         "
	print "=              made by author            "
	print "=                                        "
	print "=                                         "
	print "=               请选择您的身份：              "
	print "=             1.Administrator              "
	print "=                2.Employee                "
	print "==========================================="
	return

def Authentication_Ad():
	username = raw_input("Enter your username:")
	password = raw_input("Enter your password:")
	db = MySQLdb.connect("127.0.0.1","root","","test")
	cursor = db.cursor()
	sql = "select username from User where username = " + username + " and password = "+ password
	print sql
	cursor.execute(sql)
	data = cursor.fetchone()
	if (data != null):
		print "登陆成功！"
	else:
		print "密码或用户名不正确，登录失败"
	db.close()


def Authentication():
	op = input()
	if op == 1:
		Authentication_Ad()
	elif op == 2:
		Authentication_Em()
	else:
		return

