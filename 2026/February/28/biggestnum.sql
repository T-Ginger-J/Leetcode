-- LeetCode 619: Biggest Single Number
-- Explanation:
-- 1. A "single number" is a number that appears exactly once in the table.
-- 2. Group numbers and count occurrences.
-- 3. Keep only numbers with COUNT = 1.
-- 4. Return the maximum among them.
-- 5. If no such number exists, return NULL.
--
-- Method 1 (GROUP BY + HAVING):
-- - Use GROUP BY to count occurrences.
-- - Filter with HAVING COUNT(*) = 1.
-- - Apply MAX().
--
-- Time Complexity: O(N)
--   N = number of rows.
-- Space Complexity: O(N)
--   For grouping.
--
-- Alternative Method 1 (Subquery):
-- - First find all single numbers.
-- - Then apply MAX().
--
-- Alternative Method 2 (Window Function):
-- - Use COUNT() OVER(PARTITION BY num).
-- - Filter where count = 1.


-- Main Solution: GROUP BY + HAVING
SELECT
    MAX(num) AS num
FROM MyNumbers
GROUP BY num
HAVING COUNT(*) = 1;

