-- LeetCode 177: Nth Highest Salary
-- Explanation:
-- 1. Create a function NthHighestSalary(N).
-- 2. Select DISTINCT salaries, ordered descending.
-- 3. Use LIMIT 1 OFFSET N-1 to skip N-1 rows.
-- 4. Return NULL if result doesn’t exist.
-- Time Complexity: O(n log n)
-- Space Complexity: O(1)

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
SET N = N-1;
  RETURN (
    SELECT DISTINCT Salary
    FROM Employee
    ORDER BY Salary DESC
    LIMIT 1 OFFSET N
  );
END;

