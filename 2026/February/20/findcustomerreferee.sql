
SELECT c.name
FROM Customer c
LEFT JOIN Customer r ON c.referee_id = r.id AND r.id = 2
WHERE r.id IS NULL;
