# Write your MySQL query statement below
select d.name as Department, e.name as Employee, e.salary AS Salary
from Employee e join Department d on e.departmentid=d.id
JOIN (
    SELECT 
        departmentId,
        MAX(salary) AS max_salary
    FROM Employee
    GROUP BY departmentId
) m
    ON e.departmentId = m.departmentId
    AND e.salary = m.max_salary;