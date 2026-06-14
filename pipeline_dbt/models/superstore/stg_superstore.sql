 SELECT
    `Order ID` as order_id,
    Category,
    `Sub-Category` as sub_category,
    Sales,
    Profit,
    Quantity
FROM {{ source('sales_data', 'Superstore_raw') }}
