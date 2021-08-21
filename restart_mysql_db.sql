-- configuración MySQL database server

DROP DATABASE IF EXISTS devco_db;
CREATE DATABASE IF NOT EXISTS devco_db;
CREATE USER IF NOT EXISTS 'devco_dev'@'localhost' IDENTIFIED BY 'Devco_pwd';
GRANT ALL PRIVILEGES ON `devco_db`.* TO 'devco_dev'@'localhost';
FLUSH PRIVILEGES;