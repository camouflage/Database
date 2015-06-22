#coding=utf-8
import MySQLdb
import SharedVar
from Authentication import *
from AdminOperation import *
from EmpOperation import *

def main():
	"""
		main
	"""
	print "=========================================="
	print "=         欢迎使用 HELEN 酒店管理系统         " 
	print "=                                         "
	print "=            made by the authors            "
	print "=========================================="

	authentication = Authentication()

	SharedVar.init()

	if authentication == 0:
		pass
	elif authentication == 1:
		AdminOp()
	elif authentication == 2:
		EmpOp()

	SharedVar.commit()
	
if __name__ == "__main__":
	main()