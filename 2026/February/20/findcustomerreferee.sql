--LeetCode 584: Find Customer Referee

-- SQL Solution: Customers referred by anyone except id=2 or not referred
-- Explanation:
-- 1. We perform a LEFT JOIN on the same Customer table to check if a customer was referred by id=2.
--    - c.referee_id = r.id AND r.id = 2 ensures the join only matches referrals by customer 2.
-- 2. WHERE r.id IS NULL selects:
--    - customers not referred at all (referee_id IS NULL)
--    - customers referred by anyone except id=2 (because the join fails)
-- 3. Using LEFT JOIN + IS NULL is more efficient than filtering with "!= 2" directly,
--    because negative conditions prevent index usage.
-- Time Complexity: 
--    - O(n) in the number of customers (n = number of rows in Customer table) 
--      for scanning and joining, assuming an index on Customer.id.
-- Space Complexity:
--    - O(n) for storing the intermediate join result.

SELECT c.name
FROM Customer c
LEFT JOIN Customer r ON c.referee_id = r.id AND r.id = 2
WHERE r.id IS NULL;
