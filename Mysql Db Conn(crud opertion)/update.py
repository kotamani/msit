import connection
update = "update emp3 set name='manoj' where name='rteja'"
connection.mycursor.execute(update)
connection.mydb.commit()
