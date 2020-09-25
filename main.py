
import os
import pymysql.connections
import sys

__author__="sn.lionel90"
print(__author__)

def menu():
    os.system('cls')
    print("Choose one option for Database Management")
    print("\t1 - Insert or create new user into Data Base")
    print("\t2 - Show Data from table")
    print("\t3 - Update User data")
    #print ("\t4 - Delete user data")
    print("\t9 - Exit")

while True:
    menu()
    opcionmenu = input("What do you want to do? ")
    if opcionmenu == "1":
        print("New user")
        import pymysql
        con = pymysql.connect(host="localhost", user="root", passwd="", db="my_python")
        myCursor = con.cursor()

        sql = ('INSERT INTO userData  VALUES(0,"%s","%s","%s","%s","%s")')
        name = input("Write your name: ")
        surname = input("Write your surname: ")
        address = input("Write your home/bussines addrees: ")
        age = int(input("Write your age: "))
        email = input("Write your e-mail , maximum 150 characters: ")

        myCursor.execute(sql, (name, surname, address, age, email))
        print(" ->Data save Successfully")
        print("Your data is saved securely according the Personal Data Protection Law")
        con.commit()
        con.close()

    elif opcionmenu == "2":
        import pymysql
        print("Show Query")
        con2 = pymysql.connect(host="localhost", user="root", passwd="", db="my_python")
        myCursor2 = con2.cursor()
        myCursor2.execute("SELECT * FROM userData")
        print(myCursor2.description)
        print()

        for row in myCursor2:
            print(row)

        myCursor2.close()
        con2.close()
        input("Data Shown , Press any Key to continue")

    elif opcionmenu == "3":
        print("Update an user data")
        con3  = pymysql.connect(host="localhost", user="root", passwd="", db="my_python")
        myCursor3 = con3.cursor()
        sql3 = ('UPDATE userData SET name = %s WHERE name = %s')
        name = input("place a new name")
        myCursor3.execute(sql3, (name))
        input("data updated.., Press any Key to continue")
        con3.commit()
        con3.close()


    elif opcionmenu == "9":
        break
    else:
        print("")
        input("No option selected or wrong!...Press any Key to continue")
