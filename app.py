from ast import dump
import os, sys
from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
from werkzeug.utils import secure_filename
from controllers.ControllerApp import ControllerApp
from models.models import  setup_db, Article
from controllers.ControllerApp import *

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mysqldb import MySQL


app = Flask(__name__)
UPLOAD_FOLDER = '/static/files/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config["SQLALCHEMY_DATABASE_URI"]= "postgresql://postgres:motdepasse@localhost:5432/flask"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db = SQLAlchemy(app)
migrate = Migrate(app, db)




controllers = ControllerApp()
# setup_db(app)


def aleatoire():
    number_of_strings = 6
    length_of_string = 8
    textes = ''
    for x in range(number_of_strings):
        textes = textes+(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))
    return textes

class Article(db.Model):
    __tablename__= "articles"

    id = db.Column(db.Integer, primary_key=True)
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




@app.route('/')
def index():
    articles = [ article.format() for article in Article.query.all()]
    return controllers.index(articles)

@app.route('/add')
def add():
    return controllers.add()
@app.route('/articles')
def article():
    return jsonify({"data": "success"})

@app.route('/articles/add', methods=['POST'])
def add_article():
    if 'image' not in request.files:
            abort(400)
    file = request.files['image']
    nom =aleatoire()
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        fn = getattr(sys.modules['__main__'], '__file__')                  
        file.save("static/files/"+secure_filename(nom+".jpg"))

    article  = Article(title=request.form["title"], content = request.form["content"], photo=nom+".jpg")
    article.insert()
    data = [data.format() for data in Article.query.all()]
    return redirect(url_for('add'))



if __name__ == '__main__':
    app.run(port=3000, debug=True)
