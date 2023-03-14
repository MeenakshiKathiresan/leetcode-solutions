# Write your MySQL query statement below

select firstName, lastName, city, state 
from  address a right join person p on a.personId = p.personId