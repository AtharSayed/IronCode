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
# mycursor.execute("INSERT INTO Test (name,created,gender)VALUES (%s,%s,%s)",("SELINA",datetime.now(),"F"))# mycursor.execute("INSERT INTO Test (name,created,gender)VALUES (%s,%s,%s)",("TIM",datetime.now(),"M"))
# mycursor.execute("INSERT INTO Test (name,created,gender)VALUES (%s,%s,%s)",("STANNIS",datetime.now(),"M"))# mycursor.execute("INSERT INTO Test (name,created,gender)VALUES (%s,%s,%s)",("TIM",datetime.now(),"M"))

# mydb.commit()
# mycursor.execute("SELECT * FROM Test WHERE gender = 'M' LIMIT 1")
# mycursor.fetchone()  
# mycursor.execute("SELECT * FROM Test WHERE gender = 'F' ORDER BY name DESC")
# mycursor.execute("ALTER TABLE Test ADD COLUMN food varchar(50) NOT NULL ")
# mycursor.execute("DESCRIBE Test")
# print(mycursor.fetchone())
# print(mycursor.fetchone())

mycursor.execute("DESCRIBE Test")

for x in mycursor:
    print(x)
