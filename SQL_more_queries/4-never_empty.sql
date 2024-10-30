-- Script that creats the table id_not_nul on your MySQL server
CREATE TABLE IF NOT EXISTS `id_not_null`(
  `id` INT DEFAULT 1, `name` VARCHAR(256) NOT NULL);
