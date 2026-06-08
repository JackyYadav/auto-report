import pandas as pd
from datetime import datetime

# Load data
df = pd.read_csv("sales_data.csv")

# Summary
total = df["sales"].sum()
average = df["sales"].mean()
best_product = df.groupby("product")["sales"].sum().idxmax()
best_sales = df.groupby("product")["sales"].sum().max()

# Log output
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

output = f"""
--- Report Run: {timestamp} ---
Total Sales:     {total}
Average Sale:    {average:.2f}
Best Product:    {best_product} ({best_sales})
"""

print(output)

# Write to log file
with open("report_log.txt", "a") as f:
    f.write(output)