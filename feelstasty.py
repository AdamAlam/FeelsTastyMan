from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = "918828023105ed02141c31eb71b06497"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(35), nullable=False)
    l_name = db.Column(db.String(35), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.png')
    # gen*der = db.Column(BooleanField(), nullable=True)
    birthdate = db.Column(db.String(10))
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.l_name}', '{self.f_name}', '{self.username}', '{self.email}, '{self.image_file}'', '{self.birthdate}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    caption = db.Column(db.Text, nullable=True)
    img_posted = db.Column(db.String(120), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post(title = '{self.title}', date posted = '{self.date_posted}', caption = '{self.caption}', image posted = '{self.img_posted}', rating='{self.rating}', author = '{self.user_id}')"


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('New Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


@app.route("/")
def home():
    return render_template("home.html", title="FeelsHomeMan")


@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'adam@test.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('main'))
        else:
            flash('Login Unsuccessful. Please try again.', 'danger')
    return render_template("login.html", title="FeelsLoginMan", form=form)


@app.route('/register', methods=["POST", "GET"])
def register():
    form = RegistrationForm()
    # if request.method == "Post" and form.validate():
    #     user = User(form.username.data, form.email.data, form.password.data)
    #     db.session.add(user)
    #     return redirect(url_for('login'))
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}! Proceed to Login!', 'success')
    return render_template("register.html", title='FeelsRegisterMan', form=form)


@app.route("/about")
def about():
    return render_template("about.html", title="FeelsCuriousMan")


@app.route("/main")
def main():
    return render_template("main.html", title="FeelsTastyMan")
