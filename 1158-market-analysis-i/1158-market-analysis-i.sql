# Write your MySQL query statement below
SELECT 
    users.user_id as buyer_id, 
    users.join_date, 
    count(orders.order_id) as orders_in_2019
FROM 
    users 
LEFT JOIN 
    orders on users.user_id = orders.buyer_id
 
    AND orders.order_date >= '2019-01-01' 
    AND orders.order_date <= '2019-12-31'
GROUP BY 
    users.user_id