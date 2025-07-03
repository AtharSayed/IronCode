import mysql.connector
from datetime import datetime 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database = "testdatabase"
)

mycursor =mydb.cursor()

# mycursor.execute("CREATE TABLE Test (name varchar(50),created datetime, gender ENUM('M','F'),id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")
# mycursor.execute("INSERT INTO Test (name,created,gender)VALUES (%s,%s,%s)",("TIM",datetime.now(),"M"))
# mycursor.execute("INSERT INTO Test (name,created,gender)VALUES (%s,%s,%s)",("SELINA",datetime.now(),"F"))
# mydb.commit()
mycursor.execute("SELECT * FROM Test WHERE gender ='M'")
for x in mycursor:
    print(x)
