# Write your MySQL query statement below
-- first name, last name, city and state of each person if info not present return null.

SELECT p.firstName, p.lastName, a.city, a.state 
FROM Person as p
LEFT JOIN Address as a
ON p.personId = a.personId;