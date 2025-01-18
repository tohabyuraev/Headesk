import os
import sqlite3
import csv


path = os.path.abspath('./')
# Connecting to the geeks database
conn = sqlite3.connect(
    'headesk.sqlite'
)

with open(
    './sql/create.sql'
) as fin:
    script_create = fin.read()
conn.executescript(
    script_create
)
conn.commit()
with open(
    './sql/data.sql',
    encoding='utf-8'
) as fin:
    script_create = fin.read()
conn.executescript(
    script_create
)
conn.commit()


def insert_to_db(script, data, d=';'):
    with open(
        script
    ) as fin:
        sql = fin.read()
    with open(
        data, encoding='utf-8'
    ) as fin:
        content = csv.reader(
            fin, delimiter=d
        )
        conn.executemany(
            sql, content
        )
        conn.commit()
    

insert_to_db(
    './sql/categories.sql',
    './sql/categories.csv'
)
insert_to_db(
    './sql/etasks.sql',
    './sql/etasks.csv'
)
insert_to_db(
    './sql/etypes.sql',
    './sql/etypes.csv'
)
insert_to_db(
    './sql/marks.sql',
    './sql/marks.csv'
)
insert_to_db(
    './sql/moduls.sql',
    './sql/moduls.csv'
)
insert_to_db(
    './sql/users.sql',
    './sql/users.csv'
)
insert_to_db(
    './sql/cities.sql',
    './sql/cities.csv', d=','
)
insert_to_db(
    './sql/universities.sql',
    './sql/universities.csv', d=';'
)
insert_to_db(
    './sql/rescue_centers.sql',
    './sql/rescue_centers.csv', d=';'
)
# Reading the contents of the
# objecta.csv file

rows = conn.execute(
    """
        SELECT lat, lon
        FROM cities
        WHERE  name = 'Казань'
    """
).fetchone()
 
# Output to the console screen
for r in rows:
    print(r)
 
# Committing the changes
conn.commit() 
# closing the database connection
conn.close()