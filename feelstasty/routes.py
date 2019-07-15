from flask import render_template, url_for, redirect, flash
from feelstasty import app
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
    # if request.method == "Post" and form.validate():
    #     user = User(form.username.data, form.email.data, form.password.data)
    #     db.session.add(user)
    #     return redirect(url_for('login'))
    if form.validate_on_submit():
        flash(
            f'Account Created for {form.username.data}! Proceed to Login!', 'success')
    return render_template("register.html", title='FeelsRegisterMan', form=form)


@app.route("/about")
def about():
    return render_template("about.html", title="FeelsCuriousMan")


@app.route("/main")
def main():
    return render_template("main.html", title="FeelsTastyMan")
