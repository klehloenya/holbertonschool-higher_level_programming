--script that lists the name of records with the same score in the table second_table of the database hbtn_oc_0 in your MySQL server

USE hbtn_0c_0;
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;

