SELECT 
    Category,
    `Sub-Category` as Sub_Category,
    SUM(Sales) as total_sales,
    SUM(Profit) as total_profit,
    COUNT(`Order ID`) as total_orders
FROM {{ source('sales_data', 'Superstore_raw') }}
GROUP BY Category, `Sub-Category`
ORDER BY total_sales DESC