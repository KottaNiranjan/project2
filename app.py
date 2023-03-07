from flask import Flask,render_template,request
import numpy as np
import pickle
from database import engine
from sqlalchemy import text

# helo=[
#     {
#     "name":"Niranjan",
#     "password":1234
#     },
#     {
#     "name":"Manoj",
#     "password":123421
#     },
#     {
#     "name":"Dinesh",
#     "password":12345678
#     }
# ]


app=Flask(__name__)

model = pickle.load(open('Kidney.pkl', 'rb'))



# def load_login():
#     with engine.connect() as conn:
#         result = conn.execute(text("select * from login"))
#         login=[]
#         for row in result.all():
#             login.append(row._asdict())
@app.route("/")
def ro():
    return render_template("login.html")

# @app.route("/")
# def ro():
#     return render_template("index.html")

# @app.route("/ind")
# def ind():
#     return render_template("index.html")
# @app.route("/register")
# def load_login():
#     return render_template("register.html")
# @app.route("/login")
# def log():
#     return render_template("login.html")
@app.route("/",methods=['POST'])
def getvalue():
    login=[]
    try:
        with engine.connect() as conn:
            result = conn.execute(text("select * from login"))
            for row in result.all():
                login.append(row._asdict())
    except:
        login=[{'id': 1, 'username': 'niranjan', 'pass': 'Niranjan@8822', 'email': 'kottaniranjan8822@gmail.com'}, 
        {'id': 2, 'username': 'mani', 'pass': 'mani@123', 'email': 'mani123@gmail.com'}, 
        {'id': 3, 'username': 'yaseen', 'pass': 'yaseen@123', 'email': 'yaseen@gmail.com'}, 
        {'id': 4, 'username': 'manoj', 'pass': 'manoj0311', 'email': 'manoj@gmail.com'}]
    

    us=request.form['user']
    pa=request.form["pass"]
    for i in login:
        if us=='admin':
            return render_template("administrator.html",login=login)
        if i['username']==us:
            if i['pass']==pa:
                # with engine.connect() as conn:
                #     result = conn.execute(text("select * from login"))
                #     login=[]
                #     for row in result.all():
                #         login.append(row._asdict())
                return render_template("login.html",login=login)
                # return render_template("administrator.html")
            else:
                return render_template("login.html",s="Invalid Login Details!!")
        else:
            return render_template("login.html",s="Invalid Login Details!!")
    return render_template("administrator.html")

# @app.route("/",methods=["POST"])
# def predict():
#     sg = float(request.form['sg'])
#     htn = float(request.form['htn'])
#     hemo = float(request.form['hemo'])
#     dm = float(request.form['dm'])
#     al = float(request.form['al'])
#     appet = float(request.form['appet'])
#     rc = float(request.form['rc'])
#     pc = float(request.form['pc'])

#     values = np.array([[sg, htn, hemo, dm, al, appet, rc, pc]])
#     prediction = model.predict(values)

#     return render_template('result.html', prediction=prediction)

# @app.route("/")
# def load_login():
#     with engine.connect() as conn:
#         result = conn.execute(text("select * from login"))
#         login=[]
#         for row in result.all():
#             login.append(row._asdict())
#     return render_template("adminstrator.html",login=login)





# app.route("/api/helo")
# def g():
#     return "Hello"


# def hell():
#     return render_template("result.html")
try:
    if __name__=="__main__":
        app.run(debug=True)
except:
    pass