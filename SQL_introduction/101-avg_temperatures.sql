-- Script to display the average temperature by city in descending order
SELECT * FROM temperatures WHERE temperatures IS NULL;
SELECT city, AVG(temperatures) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
