-- SQL Solution: Investments in 2016

-- Explanation:
-- 1. Condition 1: tiv_2015 value is shared by two or more policyholders.
--    - Use a GROUP BY tiv_2015 and HAVING COUNT(*) > 1 to find duplicates.
-- 2. Condition 2: (lat, lon) pair is unique among all policyholders.
--    - Use a GROUP BY (lat, lon) and HAVING COUNT(*) = 1 to find unique locations.
-- 3. Filter Insurance table using both conditions and sum tiv_2016.
-- 4. Round the sum to 2 decimal places as required.
-- Time Complexity: O(n), n = number of policies (scans and groupings)
-- Space Complexity: O(n) for intermediate grouped results

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
