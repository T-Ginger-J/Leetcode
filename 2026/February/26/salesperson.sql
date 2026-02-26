-- LeetCode 607 style: Salespersons with no orders to "RED"
-- Explanation:
-- 1. Join Orders with Company to know which orders belong to "RED".
-- 2. Find all sales_ids that have orders for "RED".
-- 3. Select all salespersons whose sales_id is NOT in that list.
-- 4. Time Complexity: O(n)
-- 5. Space Complexity: O(n)

SELECT name
FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT DISTINCT o.sales_id
    FROM Orders o
    JOIN Company c ON o.com_id = c.com_id
    WHERE c.name = 'RED'
);