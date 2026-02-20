SELECT ROUND(SUM(i.tiv_2016), 2) AS tiv_2016
FROM Insurance i
JOIN (
    -- tiv_2015 values with duplicates
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
) t ON i.tiv_2015 = t.tiv_2015
JOIN (
    -- unique (lat, lon) pairs
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
) loc ON i.lat = loc.lat AND i.lon = loc.lon;
