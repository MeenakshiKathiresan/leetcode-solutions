# Write your MySQL query statement below
SELECT R.contest_id, round(count(*)/ 
(select count(*) from users) * 100,2) as percentage
FROM register R
GROUP BY R.contest_id 
ORDER BY percentage DESC, R.contest_id ASC
