"""
Create database with table 'demo' with sqlite3 and perform various queries.
"""

import sqlite3

# Open connection:
conn = sqlite3.connect('demo_data.sqlite3')

def create_db():
    """
    Creates a new database, table and cursor in sqlite3.
    """
    curs = conn.cursor()
    curs.execute('DROP TABLE demo;')
    table_query = 'CREATE TABLE demo(s VARCHAR(1), x INT, y INT);'
    curs.execute(table_query)

    insert_query = """
    INSERT INTO demo (s, x, y)
    VALUES ('g', 3, 9), ('v', 5, 7), ('f', 8, 7);
    """
    curs.execute(insert_query)
    #Close connection:
    curs.close()
    conn.commit()

def make_queries():
    """
    Executes various queries to find information in table.
    """
    curs = conn.cursor()

    query1 = 'SELECT COUNT(*) FROM demo;'
    results = curs.execute(query1).fetchone()[0]
    print('There are {} rows in the table.'.format(results))
    # TERMINAL OUTPUT: There are 3 rows in the table.

    query2 = """
        SELECT COUNT(*)
        FROM demo
        WHERE x >=5 AND y >=5;
        """
    results2 = curs.execute(query2).fetchone()[0]
    print('There are {} rows where x and y are at least 5.'.format(results2))
    # TERMINAL OUTPUT: There are 2 rows where x and y are at least 5.

    query3 = 'SELECT COUNT(DISTINCT y) FROM demo;'
    results3 = curs.execute(query3).fetchone()[0]
    print('There are 2 unique values in y.'.format(results3))
    # TERMINAL OUTPUT: There are 2 unique values in y.


if __name__ == "__main__":
    create_db()
    make_queries()
