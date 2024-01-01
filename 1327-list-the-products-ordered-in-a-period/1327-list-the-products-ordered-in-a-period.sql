# Write your MySQL query statement below
SELECT P.Product_name, SUM(unit) as unit
FROM Products P 
INNER JOIN Orders O
ON P.product_id = O.product_id
WHERE MONTH(order_date) = 2 AND YEAR(order_date) = 2020
GROUP by P.product_id, P.product_name
HAVING SUM(unit) > 99