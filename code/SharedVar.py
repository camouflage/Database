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
    db.close()

    UserId = data[0]
    RoomId = data[1]
    GId = data[2]
    ResId = data[3]

<<<<<<< HEAD
def commit():
    """
        commit global variable
    """
    global UserId
    global RoomId
    global GId
    global ResId

    db = MySQLdb.connect("127.0.0.1", "root", "", "test")
    cursor = db.cursor()
    sql = "UPDATE Global SET UserId = '%d', RoomId = '%d', GId = '%d', ResId = '%d'" % (UserId, RoomId, GId, ResId)

    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    db.close()
=======
    db.close();
>>>>>>> origin/master
