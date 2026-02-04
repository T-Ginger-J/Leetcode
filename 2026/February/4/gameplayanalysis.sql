-- LeetCode 511: Game Play Analysis I
-- Method: GROUP BY + MIN
-- Time Complexity: O(n)

SELECT
    player_id,
    MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;
