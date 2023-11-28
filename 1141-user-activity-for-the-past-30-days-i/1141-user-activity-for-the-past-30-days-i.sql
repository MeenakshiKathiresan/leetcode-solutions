# Write your MySQL query statement below
SELECT activity_date as day, count(DISTINCT user_id) as active_users
FROM activity
WHERE activity_date >= '2019-06-28' AND activity_date <= '2019-07-27'
GROUP BY activity_date