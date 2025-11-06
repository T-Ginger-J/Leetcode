-- LeetCode 196: Delete Duplicate Emails
-- Explanation:
-- 1. For each email, keep only the record with the smallest Id.
-- 2. Delete all others with larger Ids.
-- Time Complexity: O(n)
-- Space Complexity: O(1)

DELETE p1
FROM Person p1
JOIN Person p2
ON p1.Email = p2.Email
WHERE p1.Id > p2.Id;
