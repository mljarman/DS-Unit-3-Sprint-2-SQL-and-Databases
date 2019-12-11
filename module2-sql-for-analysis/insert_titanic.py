import pandas as pd
import numpy as np
import psycopg2 as pg2
import sqlite3

# Read in CSV file:
df = pd.read_csv('titanic.csv')
# Just in case there's an issues with spaces and /:
df.columns = df.columns.str.replace(' ', '_')
df.columns = df.columns.str.replace('/', '_')
# To get rid of the ' in some of the names
df.Name = df.Name.str.replace("'", " ")
# To find length of longest name in Name column for table creation:
df.Name.map(lambda x: len(x)).max()

# Sqlite3 connection and cursor
sq_conn = sqlite3.connect('titanic.sqlite3')
sq_curs = sq_conn.cursor()

# Turn CSV into sqlite3 table so can turn into postgres table:
sq_curs.execute('DROP TABLE sqtitanic;')
df.to_sql('sqtitanic', con=sq_conn)

# Save it to a variable:
passengers = sq_curs.execute('SELECT * from sqtitanic;').fetchall()


# Database information from elephantSQL:
dbname = 'dbname from elephantSQL'
user = 'user from elephantSQL'
password = 'password from elephantSQL'
host = 'host from elephantSQL'

# Make connection:
pg_conn = pg2.connect(dbname=dbname, user=user, password=password, host=host)
# Make cursor:
pg_curs = pg_conn.cursor()

# need to run this code again if ever run script again:
# pg_curs.execute('DROP TYPE gender;')

# Create enumerated type for Sex
query1 = "CREATE TYPE gender AS ENUM ('male', 'female');"
pg_curs.execute(query1)

# need to run this code again if ever run script again:
# pg_curs.execute('DROP TABLE insert_titanic')

# Create insert_titanic table:
create_insert_titanic = """
CREATE TABLE insert_titanic (
Passenger_ID SERIAL PRIMARY KEY,
Survived INT,
Pclass INT,
Name VARCHAR(85),
Sex gender,
Age FLOAT,
Siblings_Spouses_Aboard INT,
Parents_Children_Aboard INT,
Fare FLOAT
);
"""
# Execute:
pg_curs.execute(create_insert_titanic)


# For loop to insert all data from sqlite3 table into postgres table:
for passenger in passengers:
    insert_passenger = """
        INSERT INTO insert_titanic
        (Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard,
        Parents_Children_Aboard, Fare)
        VALUES """ + str(passenger[1:]) + ";"
    pg_curs.execute(insert_passenger)

pg_curs.execute('SELECT * from insert_titanic;')
pg_curs.fetchall()

# Make sure rows match between 2 tables:
pg_passengers = pg_curs.fetchall()
for passenger, pg_passenger in zip(passengers, pg_passengers):
    assert passengers == pg_character

# Close connections and commit changes:
pg_curs.close()
pg_conn.commit()
sq_curs.close()
sq_conn.commit()
