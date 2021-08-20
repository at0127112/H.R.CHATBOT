from flask import Flask,render_template,request
import pymysql
from Framework import *
app = Flask(__name__)
conn=pymysql.connect(host="remotemysql.com",user="wjKlba83ij",password="ExHjbSO4i3",database="wjKlba83ij")
cursor=conn.cursor()

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/savedata",methods=['POST'])
def savedata():
    username=request.form.get('username')
    empID=request.form.get('EmpID')
    emppassword=request.form.get('Emppassword')
    us=cursor.execute("""INSERT INTO Employee_details(username,employeeID,password) VALUES(%s,%s,%s)""",(username,empID,emppassword))
    print(us)
    conn.commit()
    return render_template("login.html")

@app.route("/login_validation",methods=['POST'])
def login_validation():
    global users
    employeeID=request.form.get('Employee_ID')
    password=request.form.get('password')
    print(employeeID)
    print(password)
    cursor.execute("SELECT employeeID FROM Employee_details WHERE employeeID="+employeeID+" AND password="+password+" ")
    userID=cursor.fetchall()
    users=userID[0][0]
    print(users)
    if len(users)>0:
        return render_template("index.html")
    else:
        return render_template("login.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    print(users)
    text = in_func(userText,users)
    print(text)
    if "\n" in text:
        text = text.replace("\n","<br>")
    return str(text)

if __name__ == "__main__":    
    app.run() 
