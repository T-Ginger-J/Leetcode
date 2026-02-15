-- Calculate fraction of players who logged in the day after their first login
WITH first_login AS (
    SELECT player_id, MIN(event_date) AS first_date
    FROM Activity
    GROUP BY player_id
)

SELECT 
    ROUND(
        COUNT(*) * 1.0 / (SELECT COUNT(*) FROM first_login),
        2
    ) AS fraction
FROM first_login f
WHERE EXISTS (
    SELECT 1
    FROM Activity a
    WHERE a.player_id = f.player_id
      AND a.event_date = DATE_ADD(f.first_date, INTERVAL 1 DAY)
);
