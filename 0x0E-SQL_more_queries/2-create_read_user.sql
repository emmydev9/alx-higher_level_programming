-- create a database and a user if not exist
-- assign a privilege of only that particular database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2;
GRANT SELECT hbtn_0d_2.* TO 'user_0d_2'@'localhost' IDENTIFiED BY 'user_0d_2_pwd';
