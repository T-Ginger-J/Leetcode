FROM Stadium s1
JOIN Stadium s2 ON s2.id = s1.id + 1 AND s2.people >= 100
JOIN Stadium s3 ON s3.id = s1.id + 2 AND s3.people >= 100
WHERE s1.people >= 100

UNION

SELECT s2.id, s2.visit_date, s2.people
FROM Stadium s1
JOIN Stadium s2 ON s2.id = s1.id + 1 AND s2.people >= 100
JOIN Stadium s3 ON s3.id = s1.id + 2 AND s3.people >= 100
WHERE s1.people >= 100

UNION

SELECT s3.id, s3.visit_date, s3.people
FROM Stadium s1
JOIN Stadium s2 ON s2.id = s1.id + 1 AND s2.people >= 100
JOIN Stadium s3 ON s3.id = s1.id + 2 AND s3.people >= 100
WHERE s1.people >= 100

ORDER BY visit_date;


SELECT MAX(current_count) AS busiest_period
FROM (
    SELECT 
        time_point,
        SUM(delta) OVER (ORDER BY time_point ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS current_count
    FROM (
        SELECT enter AS time_point, 1 AS delta FROM Log
        UNION ALL
        SELECT leave AS time_point, -1 AS delta FROM Log
    ) AS events
) AS running;
