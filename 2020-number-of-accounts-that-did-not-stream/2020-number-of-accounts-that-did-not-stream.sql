# Write your MySQL query statement below

SELECT COUNT(*) AS accounts_count
FROM Subscriptions
WHERE account_id NOT IN (
    SELECT DISTINCT account_id
    FROM Streams
    WHERE YEAR(stream_date) = 2021
)
AND YEAR(start_date) <= 2021
AND YEAR(end_date) >= 2021;
