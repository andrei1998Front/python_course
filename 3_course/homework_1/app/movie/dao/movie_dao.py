import sqlite3


class MovieDAO:
    def __init__(self, path):
        self.path = path

    def get_film_by_title(self, title):
        with sqlite3.connect(self.path) as connect:
            cursor = connect.cursor()

            query = f"""
                select
                    title,
                    country,
                    release_year,
                    listed_in,
                    description
                from netflix
                where title = '{title}'
                order by release_year desc
                limit 1
            """

            response = cursor.execute(query).fetchone()

        return {
            "title": response[0],
            "country": response[1],
            "release_year": response[2],
            "genre": response[3],
            "description": response[4]
        }

    def get_films_in_range(self, yy_from, yy_to):
        films_in_range = []

        with sqlite3.connect(self.path) as connect:
            cursor = connect.cursor()

            query = f"""
                select
                    title,
                    release_year
                from netflix
                where release_year between {yy_from} and {yy_to}
            """

            cursor.execute(query)

            for row in cursor.fetchall():
                films_in_range.append({
                    "title": row[0],
                    "release_year": row[1]
                })

        return films_in_range
