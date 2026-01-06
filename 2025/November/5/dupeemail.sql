-- Explanation:
-- We have a table `Person` with columns `id` and `email`.
-- We need to find all emails that appear more than once.
-- We group by email and use HAVING COUNT(email) > 1.

SELECT 
    email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1;
