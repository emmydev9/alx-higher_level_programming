-- create a new user if not exist
-- and grant full permission to the user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost' IDENTIFIED BY "user_0d_1_pwd";
