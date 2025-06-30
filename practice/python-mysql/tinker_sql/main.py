import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database = "testdatabase"
)
mycursor = mydb.cursor("CREATE DATABASE if not exists testdatabase")
mycursor = mydb.cursor("USE testdatabase")
# mycursor.execute("CREATE TABLE Person(name VARCHAR(50), age smallint UNSIGNED, PersonID int PRIMARY KEY AUTO_INCREMENT)")

mycursor.execute("DESCRIBE Person")
for x in mycursor:
    print(x)
    
