import connection
connection.mycursor = connection.mydb.cursor()
add = "insert into emp3 (id, name, email, phone) values (%s,%s,%s,%s)";
values = [(210, 'teja', 'abc@gmail.com', 8500818680), (211, 'rteja', 'abcdd@gmail.com', 9666500467)]

connection.mycursor.executemany(add,values)
connection.mydb.commit()

connection.mycursor.execute('show databases')
a = connection.mycursor.fetchall()

print(a)