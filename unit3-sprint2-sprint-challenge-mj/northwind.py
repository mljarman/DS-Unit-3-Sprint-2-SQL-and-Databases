"""
Make connection to northwind_small DB and perform various queries.
"""
import sqlite3

# Connect to database:
conn = sqlite3.connect('northwind_small.sqlite3')


def part2_queries():
    """
    Execute queries to answer questions from different tables in DB.
    """
    curs = conn.cursor()

    query1 = """
    SELECT ProductName, UnitPrice
    FROM Product
    ORDER BY UnitPrice DESC
    LIMIT 10;
    """
    print('10 most expensive products by Unit Price:',
         curs.execute(query1).fetchall())

    """
    TERMINAL OUTPUT:
    [('Côte de Blaye', 263.5),
    'Thüringer Rostbratwurst', 123.79),
    'Mishi Kobe Niku', 97),
    "Sir Rodney's Marmalade", 81),
    'Carnarvon Tigers', 62.5),
    'Raclette Courdavault', 55),
    'Manjimup Dried Apples', 53),
    'Tarte au sucre', 49.3),
    'Ipoh Coffee', 46),
    'Rössle Sauerkraut', 45.6)]
    """

    query2 = 'SELECT AVG (2019-BirthDate) FROM Employee';
    results = curs.execute(query2).fetchone()[0]
    print('The average age of employees at the time of hire is {} years.'
          .format(round(results)))

    """
    TERMINAL OUTPUT:
    The average age of employees at the time of hire is 31 years.
    """
    query3 = """
    SELECT City, AVG(hiredate-birthdate)
    FROM Employee
    GROUP BY City
    ORDER BY City;
    """

    print('Avg age of employees at time of hire by city:',
        curs.execute(query3).fetchall())
    """
    TERMINAL OUTPUT:
    [('Kirkland', 29.0),
    ('London', 32.5),
    ('Redmond', 56.0),
    ('Seattle', 40.0),
    ('Tacoma', 40.0)]
    """


def part3_queries():
    """
    Execute queries whilst joining tables in DB.
    """
    curs = conn.cursor()

    query4 = """
    SELECT CompanyName, ProductName, UnitPrice
    FROM Product, Supplier
    WHERE Product.SupplierId = Supplier.Id
    ORDER BY UnitPrice DESC
    LIMIT 10;
    """
    print('Supplier Name, Product Name, Unit Price of 10 priciest items:',
        curs.execute(query4).fetchall())

    """
    TERMINAL OUTPUT:
    [('Aux joyeux ecclésiastiques', 'Côte de Blaye', 263.5),
    ('Plutzer Lebensmittelgroßmärkte AG', 'Thüringer Rostbratwurst', 123.79),
    ('Tokyo Traders', 'Mishi Kobe Niku', 97),
    ('Specialty Biscuits, Ltd.', "Sir Rodney's Marmalade", 81),
    ('Pavlova, Ltd.', 'Carnarvon Tigers', 62.5),
    ('Gai pâturage', 'Raclette Courdavault', 55),
    ("G'day, Mate", 'Manjimup Dried Apples', 53),
    ("Forêts d'érables", 'Tarte au sucre', 49.3),
    ('Leka Trading', 'Ipoh Coffee', 46),
    ('Plutzer Lebensmittelgroßmärkte AG', 'Rössle Sauerkraut', 45.6)]
    """

    query5 = """
    SELECT CategoryName, COUNT(DISTINCT ProductName)
    FROM Product, Category
    WHERE Product.CategoryId = Category.Id
    GROUP BY CategoryName
    ORDER BY COUNT(DISTINCT ProductName) DESC
    LIMIT 1;
    """

    print('Category with most unique products:',
         curs.execute(query5).fetchone())

    """
    TERMINAL OUTPUT
    Category with most unique products: ('Confections', 13)
    """

    query6 = """
    SELECT Employee.Id, FirstName, LastName, COUNT(TerritoryId) AS num_territories
    FROM Employee, EmployeeTerritory
    WHERE Employee.Id = EmployeeTerritory.EmployeeId
    GROUP BY Employee.Id
    ORDER BY COUNT(TerritoryId) DESC
    LIMIT 1;
    """

    print('Employee with most territories:', curs.execute(query6).fetchone())
    """
    TERMINAL OUTPUT
    Employee with most territories: (7, 'Robert', 'King', 10)
    """

if __name__ == "__main__":
    part2_queries()
    part3_queries()
