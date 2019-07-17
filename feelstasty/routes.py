from flask import render_template, url_for, redirect, flash
from feelstasty import app, db, bcrypt
from feelstasty.forms import RegistrationForm, LoginForm
from feelstasty.models import User, Post


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
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(
        f_name = form.f_name.data,
        l_name = form.l_name.data,
        birthdate = form.birthdate.data,
        gender = form.gender.data,
        username = form.username.data,
        email = form.email.data,
        password = hashed_pw
        )
        db.session.add(user)
        db.session.commit()
        flash(
            f'Your account has been created! Proceed to login!', 'success')
    return render_template("register.html", title='FeelsRegisterMan', form=form)


@app.route("/about")
def about():
    return render_template("about.html", title="FeelsCuriousMan")


@app.route("/main")
def main():
    return render_template("main.html", title="FeelsTastyMan")
