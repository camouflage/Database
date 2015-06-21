#coding=utf-8
import MySQLdb
from SharedVar import *
from Authentication import *
from AdminOperation import *

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

	SharedVar.UserId = 0
	SharedVar.RoomId = 0
	SharedVar.FacilityId = 0

	if authentication == 0:
		return 0
	elif authentication == 1:
		AdminOp()
	elif authentication == 2:
		EmpOp()

	print SharedVar.UserId, SharedVar.RoomId, SharedVar.FacilityId
	
if __name__ == "__main__":
	main()