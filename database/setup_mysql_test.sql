-- Prepare MySQL server for AgriMarket test environment

CREATE DATABASE IF NOT EXISTS agri_market_test_db;
CREATE USER IF NOT EXISTS 'agri_market_test'@'localhost' IDENTIFIED BY '[23ALX$21jkuat%17njiiri@]';
GRANT ALL PRIVILEGES ON `agri_market_test_db`.* TO 'agri_market_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'agri_market_test'@'localhost';
FLUSH PRIVILEGES;
