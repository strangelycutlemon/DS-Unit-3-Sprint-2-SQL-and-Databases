import sqlite3 as sq

conn = sq.connect('northwind_small.sqlite3')
c = conn.cursor()

print(c.execute("""select ProductName, UnitPrice
             from Product
             order by UnitPrice DESC
             limit 10;""").fetchall())

print(c.execute("""select avg(HireDate - BirthDate) from Employee;""").fetchall())

# print(c.execute(""" 
