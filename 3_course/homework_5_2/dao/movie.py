from flask import request

from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_one(self, id):
        return self.session.query(Movie).get(id)

    def get_by_director(self, director_id):
        return self.session.query(Movie).filter(Movie.director_id == director_id).all()

    def get_by_genre(self, genre_id):
        return self.session.query(Movie).filter(Movie.genre_id == genre_id)

    def get_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year)

    def post(self, req):

        nested = self.session.begin_nested()

        try:
            new_movie = Movie(**req)

            self.session.add(new_movie)
        except Exception as e:
            nested.rollback()
            raise Exception

        self.session.commit()
        return new_movie

    def put(self, movie_dict):

        nested = self.session.begin_nested()

        try:
            movie = self.get_one(movie_dict.get("id"))
            movie.title = movie_dict.get("title")
            movie.description = movie_dict.get("description")
            movie.trailer = movie_dict.get("trailer")
            movie.year = movie_dict.get("year")
            movie.rating = movie_dict.get("rating")
            movie.genre_id = movie_dict.get("genre_id")
            movie.director_id = movie_dict.get("director_id")
            self.session.add(movie)
        except Exception as e:
            nested.rollback()
            return "Ошибка!", 404

        self.session.commit()

    def delete(self, id):
        movie = self.get_one(id)

        nested = self.session.begin_nested()

        try:
            self.session.delete(movie)
        except Exception as e:
            nested.rollback()
            return "Ошибка!", 404

        self.session.commit()

