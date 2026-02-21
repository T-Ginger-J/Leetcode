-- SQL Solution: Find the customer with the most orders
-- Explanation:
-- 1. Group Orders by customer_number and count the number of orders per customer.
-- 2. Order by the count descending and pick the top 1 customer (LIMIT 1).
-- 3. Time Complexity: O(n) for scanning all orders and grouping
-- 4. Space Complexity: O(k) for grouped counts, k = number of unique customers

SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;
