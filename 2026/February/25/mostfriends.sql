-- LeetCode 602: Friend Requests II: Who Has the Most Friends
-- Explanation:
-- 1. Each friendship is bidirectional: if A is friends with B, both A and B get +1.
-- 2. We count how many friends each user has:
--    - Count requester_id as one friend for accepter_id
--    - Count accepter_id as one friend for requester_id
-- 3. Aggregate by user id and sum counts.
-- 4. Find the max number of friends.
-- 5. Time Complexity: O(n)
-- 6. Space Complexity: O(n)

WITH all_friends AS (
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id FROM RequestAccepted
),
friend_counts AS (
    SELECT id, COUNT(*) AS num
    FROM all_friends
    GROUP BY id
)
SELECT id, num
FROM friend_counts
ORDER BY num DESC
LIMIT 1;
