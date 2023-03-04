from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    #Show all statistic
    return render_template("main.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    #register user
    if request.method == "GET":
        return render_template("register.html")
    else:
        
