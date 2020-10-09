import connection
#connection.mycursor = connection.mydb.cursor()
delete = "delete from emp3 where name='teja'"
connection.mycursor.execute(delete)
connection.mydb.commit()