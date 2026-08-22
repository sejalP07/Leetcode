# Write your MySQL query statement below
SELECT(
Select distinct salary FROM Employee
order by  salary Desc
LIMIT 1 OFFSET 1
) AS SecondHighestSalary ;