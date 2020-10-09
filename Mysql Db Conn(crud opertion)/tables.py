import connection

connection.mycursor.execute('show tables')

record = connection.mycursor.fetchall()

connection.mycursor.execute('select * from emp3')
re = connection.mycursor.fetchall()
print(re)
#s = connection.mycursor.execute('d emp3')
#print(s)