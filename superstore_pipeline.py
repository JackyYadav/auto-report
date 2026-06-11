import pandas as pd
from google.cloud import bigquery
from datetime import datetime

# ── 1. Pull from BigQuery ──────────────────────────
print("Pulling Superstore data from BigQuery...")
client = bigquery.Client()

query = """
    SELECT 
        Category,
        `Sub-Category` as Sub_Category,
        SUM(Sales) as total_sales,
        SUM(Profit) as total_profit,
        COUNT(`Order ID`) as total_orders
    FROM `pipeline-learning-498907.sales_data.Superstore_raw`
    GROUP BY Category, `Sub-Category`
    ORDER BY total_sales DESC
"""

df = client.query(query).to_dataframe()
print(f"Pulled {len(df)} rows")
print(df.head())

# ── 2. Transform ───────────────────────────────────
print("Transforming...")

df["profit_margin"] = (df["total_profit"] / df["total_sales"] * 100).round(2)
df["run_date"] = datetime.now().strftime("%Y-%m-%d")

# ── 3. Save back to BigQuery ───────────────────────
print("Saving summary back to BigQuery...")

job = client.load_table_from_dataframe(
    df,
    "pipeline-learning-498907.sales_data.superstore_summary"
)
job.result()

print("Done. Table saved to BigQuery as superstore_summary")
print(df[["Category", "Sub_Category", "total_sales", "profit_margin"]].head(10))