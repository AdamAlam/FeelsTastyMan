from feelstasty import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(35), nullable=False)
    l_name = db.Column(db.String(35), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.png')
    # gender = db.Column(BooleanField(), nullable=True)
    birthdate = db.Column(db.String(10))
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.l_name}', '{self.f_name}', '{self.username}', '{self.email}, '{self.image_file}'', '{self.birthdate}')"


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