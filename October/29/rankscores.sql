-- LeetCode 178: Rank Scores
-- Explanation:
-- 1. Use DENSE_RANK() to assign rank based on descending score order.
-- 2. Identical scores share the same rank.
-- 3. Works on MySQL 8+, PostgreSQL, and Oracle (with minor syntax changes).
-- Time Complexity: O(n log n)
-- Space Complexity: O(n)

SELECT Score, DENSE_RANK() OVER (ORDER BY Score DESC) AS Rank
FROM Scores;
