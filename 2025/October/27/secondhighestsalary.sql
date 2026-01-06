-- LeetCode 176: Second Highest Salary
-- Explanation:
-- 1. Use DISTINCT to get unique salaries.
-- 2. ORDER BY salary DESC to sort from high to low.
-- 3. Use LIMIT 1 OFFSET 1 to get the second highest.
-- 4. Return NULL if no second highest exists.
-- Time Complexity: O(n log n)
-- Space Complexity: O(1)

SELECT 
    (SELECT DISTINCT Salary
     FROM Employee
     ORDER BY Salary DESC
     LIMIT 1 OFFSET 1) AS SecondHighestSalary;
