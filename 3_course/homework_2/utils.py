import sqlite3

def get_animal_by_id(animal_id, path):
    with sqlite3.connect(path) as connect:

        cursor = connect.cursor()

        query = f"""
            select
                a.*,
                o.age_upon_outcome,
                o.yy,
                o.mm,
                ot.title,
                os.title
            from (
                select 
                    a.animal_id,
                    a.animal_name,
                    a.animal_type,
                    a.date_of_birth,
                    a.animal_breed,
                    group_concat(c.title, ',') as animal_color
                from (
                    select
                        a.id as animal_id,
                        a.name as animal_name,
                        at.title as animal_type,
                        a.date_of_birth,
                        group_concat(b.title, ',') as animal_breed
                    from animal as a
                        left join animal_breed as ab
                            on a.id = ab.animal_id
                        left join breed as b
                            on ab.breed_id = b.id
                        left join animal_type as at
                            on b.type_id = at.id
                    group by   
                        a.id,
                        a.name,
                        at.title,
                        a.date_of_birth
                ) as a
                    left join animal_color as ac
                        on a.animal_id = ac.animal_id
                    left join color as c
                        on ac.color_id = c.id
                group by 
                    a.animal_id,
                    a.animal_name,
                    a.animal_type,
                    a.date_of_birth,
                    a.animal_breed
            ) as a
                left join outcome as o
                    on a.animal_id = o.animal_id
                left join outcome_detail as od
                    on o.id = od.outcome_id
                left join outcome_type as ot
                    on od.outcome_type_id = ot.id
                left join outcome_subtype as os
                    on od.outcome_subtype_id = os.id
            where a.animal_id = '{animal_id.upper()}'
        """

        result = cursor.execute(query).fetchall()
        result_list = []

        for row in result:
            result_list.append(
                {
                    "animal_id": row[0],
                    "animal_name": row[1],
                    "animal_type": row[2],
                    "date_of_birth": row[3],
                    "animal_breed": row[4],
                    "animal_color": row[5],
                    "age_upon_outcome": row[6],
                    "yy": row[7],
                    "mm": row[8],
                    "outcome_type": row[9],
                    "outcome_subtype": row[10]
                }
            )

        return result_list
