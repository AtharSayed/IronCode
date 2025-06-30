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

# Inserting values in the database 

# mycursor.execute(" INSERT INTO Person (name,age) VALUES (%s,%s)",("Tim",19))
# mycursor.execute(" INSERT INTO Person (name,age) VALUES (%s,%s)",("Joe",23))
# mycursor.execute(" INSERT INTO Person (name,age) VALUES (%s,%s)",("Rae",29))

# Commiting the values after inserting for permanent change in the database 
mydb.commit()

# Deleting the duplicate values from the table 
mycursor.execute("DELETE FROM Person WHERE name = 'Tim' ")
mydb.commit()
mycursor.execute("SELECT *FROM Person")

# mycursor.execute("DESCRIBE Person")
for x in mycursor:
    print(x)
    
