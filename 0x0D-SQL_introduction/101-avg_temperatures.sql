-- Task: Display the average temperature (Fahrenheit) by city, ordered by temperature (descending).

-- Use the hbtn_0c_0 database
USE `hbtn_0c_0`;

-- Calculate the average temperature by city and order by temperature in descending order
SELECT city, AVG(temperature) AS avg_temp
FROM temperatures -- Replace with the actual table name
GROUP BY city
ORDER BY avg_temp DESC;
