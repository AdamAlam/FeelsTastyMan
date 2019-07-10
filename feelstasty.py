from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = "918828023105ed02141c31eb71b06497"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.png')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', {self.email}, '{self.image_file}'"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text)
    img_posted = db.Column(db.String(120), nullable=False)
    rating = db.Column(db.Integer, nullable=False)


class RegistrationForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('New Password', validators=[DataRequired()])
    confirm_password = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(Form):
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('New Password', validators=[DataRequired()])
    submit = SubmitField('Login')


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
        user = User(form.username.data, form.email.data, form.password.data)
        db.session.add(user)
        return redirect(url_for('login'))
    return render_template("register.html", title='FeelsRegisterMan', form=form)
