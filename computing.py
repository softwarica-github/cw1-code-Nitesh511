import mysql.connector
import tkinter  as tk
from tkinter import *
import sys
class login:
    def __init__(self):#exception handaling
        try:
            #global decleration
            global mydb
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
            )
            cursor=db.cursor()
            cursor.execute(("CREATE DATABASE IF NOT EXISTS costumer"))

            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="costumer" #database name
            )
            mycursor=mydb.cursor()

            mycursor.execute("CREATE TABLE IF NOT EXISTS cust_info (c_id INT AUTO_INCREMENT PRIMARY KEY, c_name VARCHAR(255), phoneno VARCHAR(255),gmail VARCHAR(255),gender VARCHAR(255))")
            mycursor.execute("CREATE TABLE IF NOT EXISTS login_info (user_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), user_name VARCHAR(255),password VARCHAR(255))")



        except mysql.connector.errors.InterfaceError:
            print("open your Xampp!!")
            sys.exit()



    def sign_up(self,name,user_name,password):
        mycursor = mydb.cursor()
        print(name,user_name,password,"sdsgdhajklcnasdc")
        sql = "INSERT INTO login_info(name, user_name, password) VALUES (%s,%s,%s)"
        val = [
        (name,user_name,password),
        ]
        mycursor.executemany(sql, val)
        mydb.commit()
    def user_login(self,user_name,password):
        name_password_dict = dict()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT user_name, password FROM login_info")
        name_password = mycursor.fetchall()
        for name in name_password:
            name_password_dict[name[0]] = name[1]
        if user_name in name_password_dict and name_password_dict[user_name] == password:
            return True

    def customer_info(self,name,phonenumber,g_mail,gender):

        mycursor=mydb.cursor()
        sql="INSERT INTO cust_info(c_name,phoneno,gmail,gender) VALUES (%s,%s,%s,%s)"
        val=[
            (name,phonenumber,g_mail,gender)
        ]
        mycursor.executemany(sql,val)
        mydb.commit()
        return True

    def delete(self,del_id):
        mycursor = mydb.cursor()
        print(del_id)
        i=0
        mycursor.execute("SELECT c_id FROM cust_info")
        new_id_list=list()
        id_list=mycursor.fetchall()
        for one_id in id_list:
            new_id_list.append(str(one_id[0]))
        for x in new_id_list:
            if del_id == x:
                i=i+1
        if i == 1:
            sql ="DELETE FROM cust_info WHERE c_id = (%s) "
            val = [
                (del_id)
            ]
            mycursor.execute(sql, val)
            mydb.commit()
            return True
        if i == 0:
            return False

    def showuser(self):
        my_w = tk.Tk()
        my_w.geometry("600x600")
        cur = mydb.cursor()
        # Use all the SQL you like
        cur.execute("SELECT c_id, c_name, phoneno, gmail, gender FROM cust_info")
        # print all the first cell of all the rows
        dblist = cur.fetchall()
        print(dblist)
        i = 0
        for customer_name in dblist:
            for j in range(len(customer_name)):
                e = Entry(my_w, width=19, fg='blue')
                e.grid(row=i, column=j)
                e.insert(END, customer_name[j])
            i = i + 1
        my_w.mainloop()

