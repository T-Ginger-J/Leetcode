-- LeetCode 180: Consecutive Numbers
-- Explanation:
-- 1. Compare each row with its previous and next using LAG() and LEAD().
-- 2. If all three consecutive rows have the same Num, it qualifies.
-- 3. DISTINCT ensures we return each number only once.
-- Time Complexity: O(n)
-- Space Complexity: O(1)

SELECT DISTINCT Num AS ConsecutiveNums
FROM (
  SELECT Num,
         LAG(Num) OVER (ORDER BY Id) AS prev_num,
         LEAD(Num) OVER (ORDER BY Id) AS next_num
  FROM Logs
) t
WHERE Num = prev_num AND Num = next_num;
