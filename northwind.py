import sqlite3 as sq

# establish connection
conn = sq.connect('northwind_small.sqlite3')
c = conn.cursor()

# print 10 most expensive products
def most_expensive():
    print(c.execute("""select ProductName, UnitPrice
                 from Product
                 order by UnitPrice DESC
                 limit 10;""").fetchall())

# print average age of employee at time hired
def avg_age():
    print(c.execute("""select avg(HireDate - BirthDate) from Employee;""").fetchall())

# Stretch goal: do this at the end
# print(c.execute("""

# print 10 most expensive products and their respective suppliers
def most_expensive_suppliers():
    print(c.execute("""select Product.ProductName, Product.UnitPrice, Supplier.CompanyName
                 from Product
                 inner join Supplier on Product.SupplierID=Supplier.Id
                 order by UnitPrice DESC
                 limit 10;""").fetchall())

# print the name of the category with the most products
def biggest_category():
    print(c.execute("""select Category.CategoryName, count(distinct Product.Id)
                       from Product
                       inner join Category on Product.CategoryID=Category.Id
                       order by count(distinct Product.Id) DESC
                       limit 1;""").fetchall())
