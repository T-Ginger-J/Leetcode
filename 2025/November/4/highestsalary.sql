-- Explanation:
-- Given:
-- Employee(id, name, salary, departmentId)
-- Department(id, name)
-- We must find the employee(s) with the highest salary in each department.
-- We use a subquery to match employees whose salary equals the max salary in their department.

SELECT 
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM Employee e
JOIN Department d ON e.departmentId = d.id
WHERE (e.departmentId, e.salary) IN (
    SELECT departmentId, MAX(salary)
    FROM Employee
    GROUP BY departmentId
);
