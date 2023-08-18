-- Import in hbtn_0c_0 this table dump and displays a script in order of cities average temperature
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
