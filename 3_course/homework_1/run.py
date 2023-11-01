from flask import Flask
from app.movie.views import movie_blueprint
from app.rating.views import rating_blueprint
from app.genre.views import genre_blueprint

app = Flask(__name__)
app.config.from_pyfile('./config.py')

app.register_blueprint(movie_blueprint)
app.register_blueprint(rating_blueprint)
app.register_blueprint(genre_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
