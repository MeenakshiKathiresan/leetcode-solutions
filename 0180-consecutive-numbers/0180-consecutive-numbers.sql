# Write your MySQL query statement below
SELECT DISTINCT L1.num as ConsecutiveNums
FROM Logs L1
JOIN Logs L2 ON L1.id + 1 = L2.id AND L1.num = L2.num
JOIN Logs L3 on L1.id + 2 = L3.id AND L1.num = L3.num
