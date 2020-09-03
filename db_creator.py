import pymysql
__author__="sn.lionel90"
print(__author__)

conn = pymysql.connect(host="localhost", user= "root", passwd="", db = "my_python" )
myCursor = conn.cursor()
myCursor.execute("""CREATE TABLE userData
    (
    id int primary key AUTO_INCREMENT,
    name varchar(25),
    surname varchar(25),
    address varchar (50),
    age int (3),
    email varchar(150)
    ) 
    """)

conn.commit()
conn.close()


