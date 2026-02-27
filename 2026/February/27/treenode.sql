-- LeetCode: Tree Node
-- Explanation:
-- 1. A node is "Root" if p_id IS NULL.
-- 2. A node is "Inner" if it has a parent (p_id IS NOT NULL)
--    and also has at least one child.
-- 3. A node is "Leaf" if it has a parent but no children.
-- 4. We check children using a subquery on p_id.
-- 5. Time Complexity: O(n)
-- 6. Space Complexity: O(1)

SELECT
    t.id,
    CASE
        WHEN t.p_id IS NULL THEN 'Root'
        WHEN t.id IN (SELECT p_id FROM Tree WHERE p_id IS NOT NULL)
             THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM Tree t;
