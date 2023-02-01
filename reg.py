#!C:/Users/krajk/AppData/Local/Programs/Python/Python39/python
print("Content-Type:text/html")
print()
import cgi

form=cgi.FieldStorage()

email=form.getvalue("email")
password=form.getvalue("password")
retypepassword=form.getvalue("retypepassword")
firstname=form.getvalue("firstname")
lastname=form.getvalue("lastname")
gender=form.getvalue("gender")
country=form.getvalue("country")
terms=form.getvalue("terms")
newsletter=form.getvalue("newsletter")


import mysql.connector

con=mysql.connector.connect(user='root',password='',host='localhost',database='logindetails')
cur=con.cursor()
sql ='''create table user_info2(email VARCHAR(50),password VARCHAR(50),retypepassword VARCHAR(50),firstname VARCHAR(20),lastname VARCHAR(20),gender VARCHAR(10),country VARCHAR(50),terms VARCHAR(100),newsletter VARCHAR(200))'''
cur.execute(sql)
cur.execute("insert into user_info2(email,password,retypepassword,firstname,lastname,gender,country,terms,newsletter) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",("email","password","retypepassword","firstname","lastname","gender","country","terms","newsletter"))
con.commit()

cur.close()
con.close()
print("Registered Successfully")

import webbrowser

webbrowser.open("file:///C:/xampp/htdocs/loginpage/login.html")

