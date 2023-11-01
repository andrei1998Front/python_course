import sqlite3


class GenreDAO:
    def __init__(self, path):
        self.path = path

    def get_films_by_genre(self, genre):
        films_by_genre = []

        with sqlite3.connect(self.path) as connect:
            cursor = connect.cursor()

            query = f"""
                select
                    title,
                    description
                from netflix
                where listed_in like '%{genre}%'
                order by release_year desc
                limit 10
            """

            cursor.execute(query)

            for row in cursor.fetchall():
                films_by_genre.append({
                    "title": row[0],
                    "description": row[1]
                })

            return films_by_genre
