CREATE DATABASE IF NOT EXISTS rappidb;
CREATE USER 'dev'@'localhost' IDENTIFIED BY '0000';
GRANT ALL PRIVILEGES ON "rappidb".* TO 'dev'@'localhost';
FLUSH PRIVILEGES;
