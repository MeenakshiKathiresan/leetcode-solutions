# Write your MySQL query statement below

 
SELECT DISTINCT title
FROM Content 
INNER JOIN TVProgram 
    ON Content.content_id = TVProgram.content_id
WHERE Content.Kids_content = 'Y'
    AND Content.content_type = 'Movies'
    AND MONTH(TVProgram.program_date) = 6
    AND YEAR(TVProgram.program_date) = 2020;