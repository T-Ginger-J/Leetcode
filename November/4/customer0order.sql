-- Explanation:
-- Given tables:
-- Customers(id, name)
-- Orders(id, customerId)
-- We must find customers who have never made an order.
-- We use a LEFT JOIN and filter where Orders.id IS NULL.

SELECT 
    c.name AS Customers
FROM Customers c
LEFT JOIN Orders o ON c.id = o.customerId
WHERE o.id IS NULL;
