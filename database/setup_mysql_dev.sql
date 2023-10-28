-- Prepare MySQL server for AgriMarket

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS agri_market_db;

-- Create the user if they don't exist
CREATE USER IF NOT EXISTS 'agrimarket'@'localhost' IDENTIFIED BY 'agrimarket_pwd';

-- Grant privileges on the AgriMarket database
GRANT ALL PRIVILEGES ON `agri_market_db`.* TO 'agrimarket'@'localhost';

-- Grant SELECT privilege on the performance_schema database
GRANT SELECT ON `performance_schema`.* TO 'agrimarket'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
