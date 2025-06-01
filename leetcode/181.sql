'''
181. Employees Earning More Than Their Managers

Table: Employee
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| salary      | int     |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.
 

Write a solution to find the employees who earn more than their managers.
Return the result table in any order.
The result format is in the following example.
'''

-- Write your MySQL query statement below
SELECT worker.name AS Employee
FROM (
    Employee worker JOIN Employee manager
    ON worker.managerId = manager.id
)
WHERE worker.salary > manager.salary;