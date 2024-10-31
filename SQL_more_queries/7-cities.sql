-- Script that creates the database hbtn_0d_use and the table cities(in the database hbtn_0d_usa)on your MySQL
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT NOT NULL,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);

