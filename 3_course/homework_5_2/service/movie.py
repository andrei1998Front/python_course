from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self, filters):
        if filters["director_id"] is not None:
            return self.dao.get_by_director(filters["director_id"])
        elif filters["genre_id"] is not None:
            return self.dao.get_by_genre(filters["genre_id"])
        elif filters["year"] is not None:
            return self.dao.get_by_year(filters["year"])

        return self.dao.get_all()

    def get_one(self, id):
        return self.dao.get_one(id)

    def post(self, req):
        return self.dao.post(req)

    def put(self, movie_dict):
        self.dao.put(movie_dict)
        return self.dao

    def delete(self, id):
        self.dao.delete(id)