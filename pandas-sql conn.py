import mysql.connector
import pandas as pd

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # Replace with your MySQL username
    password="",  # Leave blank if no password is set
    database="flipkart_db"  # Replace with your database name
)

query = "SELECT * FROM flipkart_products"  # Replace with your table name
df = pd.read_sql(query, conn)

print(df.head())  # Display first few rows

# Close connection
conn.close()