import psycopg2
from getpass import getpass
import pandas as pd

# Import titanic data
df = pd.read_csv('titanic.csv')

# Set up connection to elephantsql database
dbname = 'dueuejjh'
user = 'dueuejjh'
password = getpass()
host = 'salt.db.elephantsql.com'
conn = psycopg2.connect(dbname=dbname,
                        user = user,
                        password = password,
                        host = host)
r = conn.cursor()

# Get passengers as tuples
for i in df.to_records(index=False):
    passenger = str(tuple((i[0], i[1], i[2].replace("'", ""),
                           i[3], i[4], i[5], i[6], i[7])))
    insert_passenger = """
        INSERT INTO titanic
        (Survived, Pclass, Name, Sex, Age,
        Siblings_spouses_aboard, Parents_children_aboard, Fare)
        VALUES """ + passenger + ';'
    r.execute(insert_passenger)
    # print(insert_passenger)

r.close()
conn.commit()
