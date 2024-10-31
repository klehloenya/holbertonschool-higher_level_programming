-- Script that lists all coties contained in the databse hbtn_0d_usas.

-- Thw database name will be passed as an arguement of the mysql command
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;

