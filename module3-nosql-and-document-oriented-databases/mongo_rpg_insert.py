import pymongo
import sqlite3
import pandas as pd
import numpy as np
import getpass

"""
First: send all rpg tables to MongoDB using sqlite3
"""
password = getpass()
# pull driver from mongodb
client = pymongo.MongoClient(f"mongodb://admin:{password}@glaucon-shard-00-00-qw1ix.azure.mongodb.net:27017,glaucon-shard-00-01-qw1ix.azure.mongodb.net:27017,glaucon-shard-00-02-qw1ix.azure.mongodb.net:27017/test?ssl=true&replicaSet=Glaucon-shard-0&authSource=admin&retryWrites=true&w=majority")
# make shortcut to rpg database
dbr = client.rpg
# below file path removed for privacy reasons
conn = sqlite3.connect("..LS/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/rpg_db.sqlite3")
# cursor for interacting with local rpg data in sqlite3 database
r = conn.cursor()

# get all table names from rpg
tables = r.execute("select name from sqlite_master where type='table';")
# unpack from tuples in that list
tables = list(i[0] for i in tables)

for table in tables:
    insertion = []
    columns = [i[1] for i in r.execute(
        f"pragma table_info({table});").fetchall()]
    # create json documents with columns as keys
    for i in r.execute(f"select * from {table};").fetchall():
        insertion.append(dict(zip(columns, i)))
    # we cannot insert any empty tables
    if len(insertion) > 0:
        exec(f"dbr.{table}.insert_many(insertion)")
        print(table)
        print(len(insertion))

"""
Next: upload all titanic data to MongoDB from a .CSV file.
(This is easier!)
"""

# shortcut to the only collection in the titanic database
dbt = client.titanic.titanic
# get titanic data
t_df = pd.read_csv("C:/Users/Cooper/learning/LS/DS-Unit-3-Sprint-2-SQL-and-Databases/module2-sql-for-analysis/titanic.csv")
# remove all apostrophes
t_df.Name = t_df.Name.replace("'", "")
# Send titanic data to database
columns = t_df.columns
# create json documents with columns as keys
insertion = [dict(zip(columns, i)) for i in t_df.to_records(index=False)]

# convert all numpy.int64 encoded numbers to normal integers for MongoDB
for thing in insertion:
    for k, v in thing.items():
            if isinstance(v, np.int64):
                v = int(v)
            thing[k] = v

dbt.insert_many(insertion)
