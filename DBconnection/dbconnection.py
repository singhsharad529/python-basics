import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sharad123@",
    port="3306",
    database="sharad"
)

print('connected',mydb)

mycursor=mydb.cursor()
mycursor.execute("select * from employee")

result=mycursor.fetchall()


print(result)
for db in result:
    print(db)

