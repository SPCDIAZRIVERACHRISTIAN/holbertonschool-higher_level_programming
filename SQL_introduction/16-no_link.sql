-- This is a script that lists all records of the table second_table
-- This script lists all records of the table second_table,
-- showing the score for each record regardless of the name being NULL or an empty string.
SELECT score, name FROM second_table ORDER BY score DESC;
