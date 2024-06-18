-- This script is used to select the score and name of all the students in the second_table table who have a name that is not NULL, ordered by score in descending order.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC
