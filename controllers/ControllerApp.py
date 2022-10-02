from flask import render_template, request, abort, jsonify
import os, sys
from werkzeug.utils import secure_filename
import string
import random


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def aleatoire():
    number_of_strings = 6
    length_of_string = 8
    textes = ''
    for x in range(number_of_strings):
        textes = textes+(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))
    return textes

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class ControllerApp():
    def index(self, articles):
        return render_template("index.html", name="scofield", articles= articles)
    def add(data = ''):
        return render_template("add.html")
    def add_article(Article, data=""):
         if 'image' not in request.files:
            abort(400)
         file = request.files['image']
         if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            fn = getattr(sys.modules['__main__'], '__file__')
            
            nom = aleatoire()
            file.save("static/files/"+secure_filename(nom+".jpg"))
            Article.title = request.form['title']
            Article.content = request.form['content']
            Article.photo = nom+".jpg"
            return "trucmashin"
            Article.insert(Article)
            # article = Article(title = request.form['title'], content = request.form["content"], photo = nom+".jpg")