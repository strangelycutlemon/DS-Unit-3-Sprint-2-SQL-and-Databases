import sqlite3 as sq

# establish a connection and cursor object
conn = sq.connect('demo_data.sqlite3')
r = conn.cursor()

# create the table with types
def make_demo():
    r.execute("""create table demo(
                                s varchar(1),
                                x INT,
                                y INT
                                )
    """)

# insert data from the assignment
def insert_demo():
    insert_data = """
        insert into demo
        (s, x, y)
        VALUES ('g', 3, 9), ('v', 5, 7), ('f', 8, 7);
        """
# save the changes
r.execute(insert_data)
r.close()
conn.commit()

# open a new connection
conn = sq.connect('demo_data.sqlite3')
r = conn.cursor()

# count rows
def count_rows():
    print(r.execute("select count(*) from demo").fetchall())
# count rows where x and y are both at least 5
def count_greater_than_five():
    print(r.execute("select count(*) from demo where x >= 5 and y >= 5").fetchall())
# count distinct values of y
def count_distinct_y():
    print(r.execute("select count(distinct y) from demo").fetchall())
