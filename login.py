#!C:/Users/krajk/PycharmProjects/pythonProject/venv/Scripts/python
print("Content-Type:text/html")
print()
import cgi

form=cgi.FieldStorage()

email=form.getvalue("email")
password=form.getvalue("password")

import mysql.connector
con=mysql.connector.connect(user='root',password='',host='localhost',database='logindetails')
cur=con.cursor()
cur.execute("SELECT * FROM user_info2")
row=cur.fetchall()
n=len(row)


for i in range(0,n):
    for j in range(0,1):
        global userdetail
        if((email==row[i][j]) and (password==row[i][j+1]))==True:
            userdetail=1
            break
        else:
            continue
if(userdetail):
    print("<h2>login success</h2>")

else:
    print("<h2>email or password is incorrect</h2>")

con.commit()
cur.close()
con.close()
