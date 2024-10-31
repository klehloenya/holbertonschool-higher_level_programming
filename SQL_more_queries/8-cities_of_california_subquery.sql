-- Script that lists all the cities of california that can be found in the database hbtn_0d_usa

-- The database name will be opassed as an arguement of the mysql comand
SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = (
    SELECT id 
    FROM states 
    WHERE name = 'California'
)
ORDER BY cities.id ASC;

