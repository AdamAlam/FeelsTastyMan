from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, BooleanField, StringField, PasswordField, validators

app = Flask(__name__)
app.config['SECRET_KEY'] = "918828023105ed02141c31eb71b06497"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/feelstasty'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Password must match')
    ])
    confirm = PasswordField('Repeat Password')


@app.route("/")
def home():
    return render_template("home.html", title="FeelsHomeMan")


@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template("login.html", title="FeelsLoginMan")


@app.route('/register', methods=["POST", "GET"])
def register():
    form = RegistrationForm(request.form)
    if request.method == "Post" and form.validate():
        user = User(form.username.data, form.email.datam, form.password.data)
        db_session.add(user)
        return redirect(url_for('login'))
    return render_template("register.html", title='FeelsRegisterMan', form=form)
