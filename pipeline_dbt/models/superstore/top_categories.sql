SELECT 
    Category,
    SUM(total_sales) as category_total_sales,
    SUM(total_profit) as category_total_profit,
    ROUND(SUM(total_profit) / SUM(total_sales) * 100, 2) as profit_margin_pct
FROM {{ ref('sales_by_category') }}
GROUP BY Category
ORDER BY category_total_sales DESC