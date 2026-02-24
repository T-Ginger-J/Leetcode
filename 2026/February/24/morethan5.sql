-- LeetCode 596: Classes More Than 5 Students
-- Explanation:
-- 1. We are given a table Courses(student, class).
-- 2. We need classes that have at least 5 students.
-- 3. Approach:
--    - Group by class.
--    - Count distinct students.
--    - Filter using HAVING.
-- 4. Time Complexity: O(n) over table rows
-- 5. Space Complexity: O(n) for grouping (handled internally by DB)

-- SQL Solution:

SELECT
    class
FROM Courses
GROUP BY class
HAVING COUNT(DISTINCT student) >= 5;
