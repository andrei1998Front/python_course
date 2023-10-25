from flask import Flask

from app.main.views import main_blueprint
from app.posts.views import posts_blueprint
from app.search.views import search_blueprint
from app.users.views import users_blueprint
from app.api.views import api_blueprint
from app.tag.views import tag_blueprint
from app.bookmarks.views import bookmarks_blueprint

app = Flask(__name__)

app.config.from_pyfile('./config.py')

app.register_blueprint(main_blueprint)
app.register_blueprint(posts_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(api_blueprint)
app.register_blueprint(tag_blueprint)
app.register_blueprint(bookmarks_blueprint)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>Ошибка 404! Такой страницы не существует!</h1>"


@app.errorhandler(500)
def page_not_found(e):
    return "<h1>Ошибка 500! Ошибка на стороне сервера!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
