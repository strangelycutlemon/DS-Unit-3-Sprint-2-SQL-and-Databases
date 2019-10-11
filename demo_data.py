import sqlite3 as sq

conn = sq.connect('demo_data.sqlite3')
r = conn.cursor()

r.execute("""create table demo(
                            s varchar(1),
                            x INT,
                            y INT
                            )
""")

insert_data = """
    insert into demo
    (s, x, y)
    VALUES ('g', 3, 9), ('v', 5, 7), ('f', 8, 7);
    """
r.execute(insert_data)
r.close()
conn.commit()

conn = sq.connect('demo_data.sqlite3')
r = conn.cursor()
print(r.execute("select count(*) from demo").fetchall())
print(r.execute("select count(*) from demo where x >= 5 and y >= 5").fetchall())
print(r.execute("select count(distinct y) from demo").fetchall())
