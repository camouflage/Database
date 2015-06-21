#coding=utf-8
import MySQLdb
import login

def Welcome():
	print "=========================================="
	print "=         欢迎使用 HELEN 酒店管理系统         " 
	print "=                                         "
	print "=            made by the authors            "
	print "=                                        "
	print "=                                         "
	print "=             请选择要执行的操作:            "
	#print "=                1.入住登记                "
	#print "=                2.客房查询                "
	#print "=                3.退房操作                "
	print "= 				 0. exit					  "
	print "=				 1. "
	print "==========================================="
	return

def Operate():
	while 1:
		op = input("请输入操作所对应的序号:")
		if op == 1:
			print "1"
		elif op == 2:
			print "2"
		elif op == 3:
			print "3"
		else:
			print "输入非法，请重新输入"

login.Login()
a = login.Authentication()
#Welcome()
Operate()


db = MySQLdb.connect("127.0.0.1","root","","test")

db.close()

