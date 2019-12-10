import pandas as pd
import numpy as np
import sqlite3
# from sqlalchemy import create_engine
# engine = create_engine('sqlite://', echo=False)


df = pd.read_csv('buddymove_holidayiq.csv')

# to get rid of space in column names
df.columns = df.columns.str.replace(' ', '_')

# check shape and null values to verify correctly imported dataframe.
print(df.shape)
print(df.isnull().sum())

# make connection and creare new database file.
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
df.to_sql('review', con=sqlalchemy.engine.Engine)
