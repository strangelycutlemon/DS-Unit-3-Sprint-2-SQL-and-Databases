# Data Science Unit 3 Sprint Challenge 2

## Databases and SQL

A SQL Query walks into a bar. In one corner of the bar are two tables. The Query
walks up to the tables and asks:

...

*"Mind if I join you?"*

---

In this sprint challenge you will write code and answer questions related to
databases, with a focus on SQL but an acknowledgment of the broader ecosystem.
You may use any tools and references you wish, but your final code should
reflect *your* work and be saved in `.py` files (*not* notebooks), and (along
with this file including your written answers) added to your
`DS-Unit-3-Sprint-2-SQL-and-Databases` repo.

For all your code, you may only import/use the following:
- other modules you write
- `sqlite3` (from the standard library)

As always, make sure to manage your time - get a section/question to "good
enough" and then move on to make sure you do everything. You can always revisit
and polish at the end if time allows.

This file is Markdown, so it may be helpful to add/commit/push it first so you
can view it all nice and rendered on GitHub.

Good luck!

### Part 1 - Making and populating a Database

Consider the following data:

| s   | x | y |
|-----|---|---|
| 'g' | 3 | 9 |
| 'v' | 5 | 7 |
| 'f' | 8 | 7 |

Using the standard `sqlite3` module:

- Open a connection to a new (blank) database file `demo_data.sqlite3`
- Make a cursor, and execute an appropriate `CREATE TABLE` statement to accept
  the above data (name the table `demo`)
- Write and execute appropriate `INSERT INTO` statements to add the data (as
  shown above) to the database

Make sure to `commit()` so your data is saved! The file size should be non-zero.

Then write the following queries (also with `sqlite3`) to test:

- Count how many rows you have - it should be 3!
  - ```[(3,)]```
- How many rows are there where both `x` and `y` are at least 5?
  - ```[(2,)]```
- How many unique values of `y` are there (hint - `COUNT()` can accept a keyword
  `DISTINCT`)?
  - ```[(2,)]```

Your code (to reproduce all above steps) should be saved in `demo_data.py` and
added to the repository along with the generated SQLite database.

### Part 2 - The Northwind Database

Using `sqlite3`, connect to the given `northwind_small.sqlite3` database.

![Northwind Entity-Relationship Diagram](./northwind_erd.png)

Above is an entity-relationship diagram - a picture summarizing the schema and
relationships in the database. Note that it was generated using Microsoft
Access, and some of the specific table/field names are different in the provided
data. You can see all the tables available to SQLite as follows:

```python
>>> curs.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY
name;").fetchall()
[('Category',), ('Customer',), ('CustomerCustomerDemo',),
('CustomerDemographic',), ('Employee',), ('EmployeeTerritory',), ('Order',),
('OrderDetail',), ('Product',), ('Region',), ('Shipper',), ('Supplier',),
('Territory',)]
```

*Warning*: unlike the diagram, the tables in SQLite are singular and not plural
(do not end in `s`). And you can see the schema (`CREATE TABLE` statement)
behind any given table with:
```python
>>> curs.execute('SELECT sql FROM sqlite_master WHERE name="Customer";').fetchall()
[('CREATE TABLE "Customer" \n(\n  "Id" VARCHAR(8000) PRIMARY KEY, \n
"CompanyName" VARCHAR(8000) NULL, \n  "ContactName" VARCHAR(8000) NULL, \n
"ContactTitle" VARCHAR(8000) NULL, \n  "Address" VARCHAR(8000) NULL, \n  "City"
VARCHAR(8000) NULL, \n  "Region" VARCHAR(8000) NULL, \n  "PostalCode"
VARCHAR(8000) NULL, \n  "Country" VARCHAR(8000) NULL, \n  "Phone" VARCHAR(8000)
NULL, \n  "Fax" VARCHAR(8000) NULL \n)',)]
```

In particular note that the *primary* key is `Id`, and not `CustomerId`. On
other tables (where it is a *foreign* key) it will be `CustomerId`. Also note -
the `Order` table conflicts with the `ORDER` keyword! We'll just avoid that
particular table, but it's a good lesson in the danger of keyword conflicts.

Answer the following questions (each is from a single table):

- What are the ten most expensive items (per unit price) in the database?
  ```[('Côte de Blaye', 263.5),
      ('Thüringer Rostbratwurst', 123.79),
      ('Mishi Kobe Niku', 97),
      ("Sir Rodney's Marmalade", 81),
      ('Carnarvon Tigers', 62.5),
      ('Raclette Courdavault', 55),
      ('Manjimup Dried Apples', 53),
      ('Tarte au sucre', 49.3),
      ('Ipoh Coffee', 46),
      ('Rössle Sauerkraut', 45.6)]```
- What is the average age of an employee at the time of their hiring? (Hint: a
  lot of arithmetic works with dates.)
  - ```[(37.22222222222222,)]```
- (*Stretch*) How does the average age of employee at hire vary by city?

Your code (to load and query the data) should be saved in `northwind.py`, and
added to the repository. Do your best to answer in purely SQL, but if necessary
use Python/other logic to help.

### Part 3 - Sailing the Northwind Seas

You've answered some basic questions from the Northwind database, looking at
individual tables - now it's time to put things together, and `JOIN`!

Using `sqlite3` in `northwind.py`, answer the following:

- What are the ten most expensive items (per unit price) in the database *and*
  their suppliers?
  - ```[('Côte de Blaye', 263.5, 'Aux joyeux ecclésiastiques'),
        ('Thüringer Rostbratwurst', 123.79, 'Plutzer Lebensmittelgroßmärkte AG'),
        ('Mishi Kobe Niku', 97, 'Tokyo Traders'),
        ("Sir Rodney's Marmalade", 81, 'Specialty Biscuits, Ltd.'),
        ('Carnarvon Tigers', 62.5, 'Pavlova, Ltd.'),
        ('Raclette Courdavault', 55, 'Gai pâturage'),
        ('Manjimup Dried Apples', 53, "G'day, Mate"),
        ('Tarte au sucre', 49.3, "Forêts d'érables"),
        ('Ipoh Coffee', 46, 'Leka Trading'),
        ('Rössle Sauerkraut', 45.6, 'Plutzer Lebensmittelgroßmärkte AG')]```
- What is the largest category (by number of unique products in
  it)?
  - ```[('Beverages', 77)]```
- (*Stretch*) Who's the employee with the most territories? Use
  `TerritoryId` (not name, region, or other fields) as the unique identifier for
  territories.

### Part 4 - Questions (and your Answers)

Answer the following questions, baseline ~3-5 sentences each, as if they were
interview screening questions (a form you fill when applying for a job):

- In the Northwind database, what is the type of relationship between the
  `Employee` and `Territory` tables?
  ```This is a many-to-many relationship. The EmployeeTerritory table is an
    intermediary table (aka a junction table), which is used to link the other two.
    We can easily identify such tables because they reference the primary keys of
    both tables they are joining. In this particular case, just by looking at the
    tables, we can see that an employee of this company can be assigned to multiple
    territories.```
- What is a situation where a document store (like MongoDB) is appropriate, and
  what is a situation where it is not appropriate?
  ```MongoDB would be a good choice of database for items with an indeterminate
  number of fields. For example, if a chemistry lab wanted to store information
  about experiments with many different parameters, MongoDB would be a good choice.
  It allows you to immediately start storing documents without specifying a schema.
  However, this kind of non-relational database would not be appropriate for something like an EMR (Electronic Medical Record) System, where availability is crucial.
  MongoDB is a CP system, providing no availability guarantee.
- What is "NewSQL", and what is it trying to achieve?```
  ```NewSQL is a class of database management systems that attempt to provide a relational data model together with the horizontal scalability seen in NoSQL systems. There are multiple approaches in this category, some with special architectures, others with sharding or storage engines. NewSQL is in demand because modern data-driven companies face enormous costs from planned downtime, but still require systems that can handle thousands of queries at a time, some of which are not pre-defined. These tend to be OLTP databases that prioritize availability, concurrency, and performance.```

### Part 5 - Turn it in!
Add all the files you wrote (`demo_data.py`, `northwind.py`), as well as this
file with your answers to part 4, to your weekly repo
(`DS-Unit-3-Sprint-2-SQL-and-Databases`). You're also encouraged to include the
output from your queries as docstring comments, to facilitate grading. Commit,
push, and await feedback from your PM. Thanks for your hard work!

If you got this far, check out the [larger Northwind
database](https://github.com/jpwhite3/northwind-SQLite3/blob/master/Northwind_large.sqlite.zip) -
your queries should run on it as well, with richer results.
