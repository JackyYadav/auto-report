SELECT 
    Category,
    sub_category as Sub_Category,
    SUM(Sales) as total_sales,
    SUM(Profit) as total_profit,
    COUNT(order_id) as total_orders
FROM {{ ref('stg_superstore') }}
GROUP BY Category, sub_category
ORDER BY total_sales DESC