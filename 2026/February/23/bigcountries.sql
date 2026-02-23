-- LeetCode 595: Big Countries
-- Explanation:
-- 1. We are given a table World(name, continent, area, population, gdp).
-- 2. A country is considered "big" if:
--    - area >= 3,000,000 OR
--    - population >= 25,000,000
-- 3. We must return name, population, and area for such countries.
-- 4. Use simple filtering with WHERE.
-- 5. Time Complexity: O(n) over table rows
-- 6. Space Complexity: O(1)

-- SQL Solution:

SELECT
    name,
    population,
    area
FROM World
WHERE
    area >= 3000000
    OR population >= 25000000;
