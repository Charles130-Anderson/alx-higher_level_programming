-- Script to list all cities of California using subquery

-- Select cities of California
SELECT * FROM cities
WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY id ASC;
