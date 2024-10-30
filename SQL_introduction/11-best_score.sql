--script that lists all records with a score >= 10 in the tabel seocnd of the tabase hbtn_0c_0 in your MySQL server

USE hbtn_0c_0;
SELECT score, name FROM second_table ORDER BY score DESC;



