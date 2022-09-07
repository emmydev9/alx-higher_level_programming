-- create a table with id not null with primary keys
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(id INT NOT NULL IDENTITY(1,1) PRIMARY KEY, name VARCHAR(256) DEFAULT NOT NULL);
