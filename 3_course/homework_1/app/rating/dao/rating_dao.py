import sqlite3


class RatingDao:

    def __init__(self, path):
        self.path = path

    def select_rating_group(self, rating):
        if rating == 'children':
            return "'G'"
        elif rating == 'family':
            return "'G', 'PG', 'PG-13'"
        elif rating == 'adult':
            return "'R', 'NC-17'"
        else:
            raise ValueError

    def get_film_by_rating(self, rating):
        films_by_rating = []
        rating_group = self.select_rating_group(rating)

        with sqlite3.connect(self.path) as connect:
            cursor = connect.cursor()

            query = f"""
                select 
                    title,
                    rating,
                    description
                from netflix
                where
                    rating in ({rating_group})
            """

        cursor.execute(query)

        for row in cursor.fetchall():
            films_by_rating.append({
                "title": row[0],
                "rating": row[1],
                "description": row[2]
            })

        return films_by_rating
