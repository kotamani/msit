import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', password='ravi143', database = 'salavuddin')

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE emp3 (id INT, name VARCHAR(65), email VARCHAR(65), phone BIGINT)")