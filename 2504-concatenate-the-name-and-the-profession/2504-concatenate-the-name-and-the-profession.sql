# Write your MySQL query statement below
select person_id, CONCAT(name, "(", LEFT(profession, 1),")") as name from Person
order by person_id desc