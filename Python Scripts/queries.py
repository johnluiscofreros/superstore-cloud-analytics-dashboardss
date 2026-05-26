import sqlite3
import pandas as pd

conn = sqlite3.connect("superstore.db")

# Query 1: Total sales per category
query1 = """
SELECT Category, ROUND(SUM(Sales), 2) AS total_sales
FROM superstore_sales
GROUP BY Category
ORDER BY total_sales DESC;
"""

# Query 2: Average sales per region
query2 = """
SELECT Region, ROUND(AVG(Sales), 2) AS average_sales
FROM superstore_sales
GROUP BY Region
ORDER BY average_sales DESC;
"""

# Query 3: Top 10 products by sales
query3 = """
SELECT "Product Name", ROUND(SUM(Sales), 2) AS total_sales
FROM superstore_sales
GROUP BY "Product Name"
ORDER BY total_sales DESC
LIMIT 10;
"""

print("\nQUERY 1: Total Sales per Category")
print(pd.read_sql_query(query1, conn))

print("\nQUERY 2: Average Sales per Region")
print(pd.read_sql_query(query2, conn))

print("\nQUERY 3: Top 10 Products by Sales")
print(pd.read_sql_query(query3, conn))

conn.close()