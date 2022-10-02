from turtle import title
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, false, true
# from flask_migrate import Migrate
from flask_mysqldb import MySQL


db = SQLAlchemy()


database_name = 'flask'
database_path = 'postgresql://postgres:motdepasse@{}/{}'.format('localhost:5432',  database_name)

def setup_db(app):
    # app.config['MYSQL_HOST'] = 'localhost'
    # app.config['MYSQL_USER'] = 'root'
    # app.config['MYSQL_PASSWORD'] = ''
    # app.config['MYSQL_DB'] = 'flask'
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class Article(db.Model):
    __tablename__= "articles"

    id = db.Column(db.Integer, primary_key=true)
    title = db.Column(db.String(), nullable=False)
    content = db.Column(db.String(), nullable=False)
    photo = db.Column(db.String(), nullable=True)

    def __init__(self, title, content, photo):
        self.title = title
        self.content = content
        self.photo = photo
    
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content, 
            'photo' : self.photo
        }
