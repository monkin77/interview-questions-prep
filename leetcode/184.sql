'''
184. Department Highest Salary

Table: Employee
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
id is the primary key (column with unique values) for this table.
departmentId is a foreign key (reference columns) of the ID from the Department table.
Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.
 
Table: Department
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table. It is guaranteed that department name is not NULL.
Each row of this table indicates the ID of a department and its name.
 
Write a solution to find employees who have the highest salary in each of the departments.

Return the result table in any order.
'''

-- Write your MySQL query statement below
SELECT Department.name AS Department, Employee.name AS Employee, salary As Salary
FROM (
        (
        SELECT departmentId, MAX(salary) AS maxSalary FROM Employee
        GROUP BY departmentId
        ) DeptMaxSalaries 
    INNER JOIN Employee ON DeptMaxSalaries.departmentId = Employee.departmentId ) 
    INNER JOIN Department ON Department.id = Employee.departmentId
WHERE salary = maxSalary
