import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

""" ONE TO MANY RELATIONSHIPS """

sales_reps = pd.read_sql("""
                 SELECT  firstName, lastName, email
                 FROM employees
                 WHERE jobTitle = 'Sales Rep';
                 """, conn)

# print("Number of results: ", len(sales_reps))
# print(sales_reps)

cities_of_sales_reps = pd.read_sql("""
                                   SELECT firstName, lastName, email, city
                                   FROM employees
                                   JOIN offices
                                   USING(officeCode)
                                   WHERE jobTitle = 'Sales Rep';
                                   """, conn)

# print("Number of results: ", len(cities_of_sales_reps))
# print(cities_of_sales_reps)

# When there is a one-to-many relationship, sometimes the number of records will increase to match the number of records in the larger table.
product_lines = pd.read_sql("""
                            SELECT productLine, textDescription
                            FROM productLines;
                            """, conn)

# print("Number of results: ", len(product_lines))
# print(product_lines.head())

# Now let's join that table with the products table, and select the vendor and product description.
joined_product_lines = pd.read_sql("""
                                   SELECT productLine, textDescription, productVendor, productDescription
                                   FROM productLines
                                   JOIN products
                                   USING(productLine)
                                   """, conn)

# print("Number of results: ", len(joined_product_lines))
# print(joined_product_lines.head())
# As you can see, the number of records has increased significantly, 
# because the same product line is now appearing multiple times in the results, once for each actual product.


""" MANY TO MANY RELATIONSHIPS """
just_offices = pd.read_sql("""
                           SELECT *
FROM offices
;
""", conn)

print('Number of results:', len(just_offices))
print(just_offices.head())

just_customers = pd.read_sql("""
SELECT *
FROM customers
;
""", conn)

print('Number of results:', len(just_customers))
print(just_customers.head())

offices_and_customers = pd.read_sql("""
SELECT *
FROM offices
JOIN customers
    USING(state)
;
""", conn)

print('Number of results:', len(offices_and_customers))
print(offices_and_customers.head())

conn.close()