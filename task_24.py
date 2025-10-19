# todo: добавьте во Flask маршруты для страниц (endpoint)
# - О компании
# - Контакты
# - Список постов

from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return '<p>Hello!</p>'

@app.route("/about")
def about():
    return '<p>О компании!</p>'

@app.route("/contacts")
def contacts():
    return '<p>Контакты</p>'

@app.route("/posts")
def posts():
    return '<p>Список постов</p>'