-- This is a script that lists all records of the table second_table
SELECT score, COALESCE(NULLIF(name, ''), 'No Name') AS name FROM second_table ORDER BY score DESC;
