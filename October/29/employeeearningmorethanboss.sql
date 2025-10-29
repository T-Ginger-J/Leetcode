-- LeetCode 181: Employees Earning More Than Their Managers
-- Explanation:
-- 1. Join Employee table with itself (alias e = employee, m = manager).
-- 2. Filter rows where employee’s ManagerId matches manager’s Id.
-- 3. Check if employee’s Salary > manager’s Salary.
-- 4. Return employee names that satisfy the condition.
-- Time Complexity: O(n)
-- Space Complexity: O(1)

SELECT e.Name AS Employee
FROM Employee e
JOIN Employee m ON e.ManagerId = m.Id
WHERE e.Salary > m.Salary;
