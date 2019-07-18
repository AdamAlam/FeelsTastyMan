from feelstasty import db, login_m
from datetime import datetime
from flask_login import UserMixin


@login_m.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(35), nullable=False)
    l_name = db.Column(db.String(35), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.png')
    birthdate = db.Column(db.String(), nullable=False)
    gender = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User(Last Name: '{self.l_name}', First Name: '{self.f_name}', Username: '{self.username}', Email: '{self.email}, Profile Picture: '{self.image_file}'', Birthday: '{self.birthdate}', Gender: '{self.gender}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    caption = db.Column(db.Text, nullable=True)
    img_posted = db.Column(db.String(120), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post(title = '{self.title}', date posted = '{self.date_posted}', caption = '{self.caption}', image posted = '{self.img_posted}', rating='{self.rating}', author = '{self.user_id}')"
