import pandas as pd
import sqlite3

# Load the cleaned dataset
df = pd.read_csv("cleaned_superstore.csv")

# Create/connect to SQLite database
conn = sqlite3.connect("superstore.db")

# Load data into a table named superstore_sales
df.to_sql("superstore_sales", conn, if_exists="replace", index=False)

# Check if data loaded successfully
result = pd.read_sql_query("SELECT * FROM superstore_sales LIMIT 5", conn)
print(result)

# Show total rows
count = pd.read_sql_query("SELECT COUNT(*) AS total_rows FROM superstore_sales", conn)
print(count)

conn.close()

print("Database loaded successfully!")