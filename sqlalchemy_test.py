import pandas as pd
from sqlalchemy import create_engine

# Connect to MySQL
engine = create_engine("mysql+pymysql://root:Sqldata2026@localhost:3306/mysql")

# Create sample data
data = {
    "product": ["Laptop", "Phone", "Tablet"],
    "total_sales": [3450, 2800, 1350]
}
df = pd.DataFrame(data)

# Write to MySQL
df.to_sql("sales_summary", engine, if_exists="replace", index=False)
print("Data written to MySQL")

# Read it back
result = pd.read_sql("SELECT * FROM sales_summary", engine)
print(result)