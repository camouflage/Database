#coding=utf-8
import MySQLdb

def init():
    """
        init global variable
    """
    global UserId
    global RoomId
    global GId
    global ResId

    # connect to db.
    db = MySQLdb.connect("127.0.0.1", "root", "", "test")
    cursor = db.cursor()
    sql = "SELECT * FROM Global"
    cursor.execute(sql)
    data = cursor.fetchone()

    UserId = data[0]
    RoomId = data[1]
    GId = data[2]
    ResId = data[3]
