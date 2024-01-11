# Write your MySQL query statement below
SELECT SalesPerson.name
FROM SalesPerson 
WHERE SalesPerson.sales_id NOT IN (
SELECT SalesPerson.sales_id FROM SalesPerson 
LEFT JOIN Orders ON Orders.sales_id = SalesPerson.sales_id
LEFT JOIN Company ON Company.com_id = Orders.com_id
WHERE Company.name = 'RED');

