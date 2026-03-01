-- Main Solution: GROUP BY + HAVING
SELECT
    MAX(num) AS num
FROM MyNumbers
GROUP BY num
HAVING COUNT(*) = 1;

