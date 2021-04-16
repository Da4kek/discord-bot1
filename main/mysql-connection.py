import mysql.connector 

mydb = mysql.connector.connect(
  host = "DESKTOP-workstation",
  user = "root",
  password = "Myindian@123",
  database = "discord"
)
print(mydb)