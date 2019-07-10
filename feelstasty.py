from flask import Flask, render_template, url_for

app = Flask(__name__)

app.config['SECRET_KEY'] = "918828023105ed02141c31eb71b06497"


@app.route("/")
def home():
    return render_template("home.html", title="FeelsTasty Home")

@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template("login.html", title="FeelsLoginMan")


@app.route('/register', methods=["POST", "GET"])
def register():
    return render_template("register.html", title='FeelsRegisterMan')
