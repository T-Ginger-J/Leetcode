-- LeetCode 175: Combine Two Tables
-- Explanation:
-- 1. LEFT JOIN Person and Address on PersonId.
-- 2. Select required columns: FirstName, LastName, City, State.
-- 3. If a person has no address, City and State will be NULL.
-- Time Complexity: O(n)
-- Space Complexity: O(1)

SELECT 
    Person.FirstName,
    Person.LastName,
    Address.City,
    Address.State
FROM Person
LEFT JOIN Address
ON Person.PersonId = Address.PersonId;
