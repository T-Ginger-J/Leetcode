-- LeetCode 610: Triangle Judgement
-- Explanation:
-- 1. Three line segments (x, y, z) can form a triangle if:
--    x + y > z AND x + z > y AND y + z > x
-- 2. If all three conditions are satisfied, return "Yes".
-- 3. Otherwise, return "No".
-- 4. Use a CASE statement to evaluate the triangle inequality.
--
-- Method 1 (CASE with Direct Comparison):
-- - Check all three triangle conditions in WHERE/CASE.
--
-- Time Complexity: O(N)
--   N = number of rows in Triangle table.
-- Space Complexity: O(1)
--   No extra storage used.
--
-- Alternative Method 1 (Using LEAST/GREATEST):
-- - A triangle is valid if:
--   smallest + middle > largest.
-- - Compute largest side using GREATEST.
--
-- Alternative Method 2 (Using Sorting via Expressions):
-- - Reorder sides logically and apply one inequality.
-- - Useful if extended to more sides.


-- Main Solution: Direct Triangle Inequality Check
SELECT
    x,
    y,
    z,
    CASE
        WHEN x + y > z
         AND x + z > y
         AND y + z > x
        THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM Triangle;


-- Alternative Solution 1: Using GREATEST
SELECT
    x,
    y,
    z,
    CASE
        WHEN (x + y + z) - GREATEST(x, y, z) > GREATEST(x, y, z)
        THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM Triangle;


-- Alternative Solution 2: Using LEAST and GREATEST
SELECT
    x,
    y,
    z,
    CASE
        WHEN LEAST(x, y, z)
           + (x + y + z - LEAST(x, y, z) - GREATEST(x, y, z))
           > GREATEST(x, y, z)
        THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM Triangle;


-- -------------------------
-- Examples (Not From LeetCode)
-- -------------------------

-- Example 1: All equal sides (valid)
-- Input:
-- | x | y | z |
-- | 5 | 5 | 5 |
-- Output:
-- | 5 | 5 | 5 | Yes |

-- Example 2: One side too long (invalid)
-- Input:
-- | x | y | z |
-- | 2 | 3 | 6 |
-- Output:
-- | 2 | 3 | 6 | No |

-- Example 3: Minimal valid triangle
-- Input:
-- | x | y | z |
-- | 3 | 4 | 5 |
-- Output:
-- | 3 | 4 | 5 | Yes |
