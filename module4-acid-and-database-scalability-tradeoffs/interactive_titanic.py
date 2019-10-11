import psycopg2
from getpass import getpass
import pandas as pd

# Import titanic data
df = pd.read_csv("C:/Users/Cooper/learning/LS/DS-Unit-3-Sprint-2-SQL-and-Databases/module2-sql-for-analysis/titanic.csv")

# Set up connection to elephantsql database
dbname   = 'dueuejjh'
user     = 'dueuejjh'
password = getpass()
host     = 'salt.db.elephantsql.com'
conn = psycopg2.connect(dbname   = dbname,
                        user     = user,
                        password = password,
                        host     = host)
r = conn.cursor()
