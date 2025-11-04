-- LeetCode 197: Rising Temperature
-- Explanation:
-- 1. Self-join the table to compare each date with its previous date.
-- 2. Check if current temperature is higher than the previous day's.
-- 3. Ensure record dates differ by exactly 1 day using DATEDIFF.
-- Time Complexity: O(n^2) worst case (self join)
-- Space Complexity: O(1)

SELECT w1.Id
FROM Weather w1
JOIN Weather w2
  ON DATEDIFF(w1.RecordDate, w2.RecordDate) = 1
WHERE w1.Temperature > w2.Temperature;
