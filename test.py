import pymysql
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="sanju123@",
    database="contactdb"
)
print("Connected successfully!")
