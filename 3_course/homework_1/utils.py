import sqlite3
import json
from config import DB_PATH

def get_double_actor(actor_first, actor_last):
    with sqlite3.connect(DB_PATH) as connect:
        cursor = connect.cursor()

        query = f"""
            select
                `cast`
            from netflix
            where
                `cast` like '%{actor_first}%' 
                and `cast` like '%{actor_last}%'
        """

        cursor.execute(query)

        actors = []

        for row in cursor.fetchall():
            actors.extend(row[0].split(','))

        result = []

        for actor in actors:
            if actor == actor_last or actor == actor_first:
                continue
            elif actors.count(actor) > 2:
                result.append(actor)

        return set(actors)


def get_films_by_args(type_film, yy, genre):
    films_by_args = []

    with sqlite3.connect(DB_PATH) as connect:
        cursor = connect.cursor()

        query = f"""
            select 
                title,
                description
            from netflix
            where
                release_year = {yy}
                and listed_in like '%{genre}%'
                and type = '{type_film}'
        """

        cursor.execute(query)

        for row in cursor.fetchall():
            print(row)
            films_by_args.append({
                "title": row[0],
                "description": row[1]
            })

        return json.dumps(films_by_args)
