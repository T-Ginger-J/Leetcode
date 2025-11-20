-- LeetCode 262: Trips and Users
-- Explanation:
-- 1. Join Trips with Users twice (client and driver)
-- 2. Filter unbanned users
-- 3. Group by request_at and calculate cancellation rate
-- 4. Round to 2 decimal points

SELECT
    t.request_at AS Day,
    ROUND(
        SUM(CASE WHEN t.status LIKE 'cancelled%' THEN 1 ELSE 0 END) * 1.0 / COUNT(*), 2
    ) AS "Cancellation Rate"
FROM Trips t
JOIN Users c ON t.client_id = c.users_id
JOIN Users d ON t.driver_id = d.users_id
WHERE c.banned = 'No' AND d.banned = 'No'
  AND t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY t.request_at;
