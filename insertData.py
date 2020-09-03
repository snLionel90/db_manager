import pymysql
import os
import pymysql.connections
import sys

__author__="sn.lionel90"
print(__author__)

con = pymysql.connect(host="localhost", user= "root", passwd="", db = "my_python" )
myCursor = con.cursor()

sql = ('INSERT INTO userData  VALUES(0,"%s","%s","%s","%s","%s")')
name = input("Write your name: ")
surname = input("Write your surname: ")
address = input("Write your home/bussines addrees: ")
age = int(input("Write your age: "))
email = input("Write your e-mail , maximum 150 characters: ")

myCursor.execute(sql,(name,surname,address,age,email))
print(" ->data instaled")
print("Your data is saved securely according the Personal Data Protection Law")
con.commit()
con.close()


