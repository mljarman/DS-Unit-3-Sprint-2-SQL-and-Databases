"""
Titanic questions with PostgreSql
"""
import psycopg2

# Connect to ElephantSQL:
dbname = 'wgxzavuq'
user = 'wgxzavuq'
password = 'QHBX6GpDZWt0HSB9Rz_8sohQcGE7uAMH'
host = 'rajje.db.elephantsql.com'

# Make connection and create cursor:
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
curs = conn.cursor()

curs.execute('SELECT * FROM insert_titanic')

def titanic_queries():
    """
    Runs multiple queries to answer various questions.
    """
# How many passengers survived, how many died?
    query1 = """
        SELECT Survived, COUNT(*)
        FROM insert_titanic
        GROUP BY Survived;
        """
    curs.execute(query1)
    print('Passengers who did not survive and did:', curs.fetchall())
# How many passengers were in each class?
    query2 = """
        SELECT Pclass, COUNT(*)
        FROM insert_titanic
        GROUP BY Pclass;
        """
    curs.execute(query2)
    print('Passengers split by class:', curs.fetchall())
# How many passengers survived/died within each class?
    query3 = """
        SELECT Pclass, Survived, Count(*)
        FROM insert_titanic
        GROUP BY Pclass, Survived
        ORDER BY Pclass;
        """
    curs.execute(query3)
    print('Passengers split by class, then surived:', curs.fetchall())
# What was average age of survivors vs nonsurvivors?
    query4 = """
        SELECT Survived, AVG(age) as Avg_Age
        FROM insert_titanic
        GROUP BY Survived;
        """
    curs.execute(query4)
    print('Average age of nonsurvivors and survivors:', curs.fetchall())
# What was the average age of each passenger class?
    query5 = """
        SELECT Pclass, AVG(Age) AS Avg_Age
        FROM insert_titanic
        GROUP BY Pclass
        ORDER BY Pclass;
        """
    curs.execute(query5)
    print('Average age of passengers by class:', curs.fetchall())
# What was the average fare by passenger class? By surived?
    query6 = """
        SELECT Pclass, Survived, AVG(fare) as Avg_Fare
        FROM insert_titanic
        GROUP BY Pclass, Survived
        ORDER by Pclass;
        """
    curs.execute(query6)
    print('Average fare by class:', curs.fetchall())
# How many siblings/parents aboard on average by class? By survived?
    query7 = """
        SELECT Pclass, Survived, AVG(Siblings_Spouses_Aboard)
        AS Avg_Siblings_Spouses_Aboard
        FROM insert_titanic
        GROUP BY Pclass, Survived
        ORDER BY Pclass;
        """
    curs.execute(query7)
    print('Average fare by class:', curs.fetchall())
# How many parents/children aboard on average by class? By survived?
    query8 = """
        SELECT Pclass, Survived, AVG(Parents_Children_Aboard)
        AS Avg_Parents_Children_Aboard
        FROM insert_titanic
        GROUP BY Pclass, Survived
        ORDER BY Pclass;
        """
    curs.execute(query8)
    print('Average fare by class:', curs.fetchall())
# Do any passengers have the same name?
    query9 = """
        SELECT COUNT(*) - COUNT(DISTINCT(Name))
        FROM insert_titanic;
        """
    curs.execute(query9)
    results = curs.fetchone()[0]
    if (results > 0):
        print('Number of same names: {}'.format(results))
    else:
        print('No same names')



if __name__ == "__main__":
    titanic_queries()
