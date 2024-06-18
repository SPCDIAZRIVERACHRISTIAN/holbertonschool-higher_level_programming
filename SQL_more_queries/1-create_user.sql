-- This script creates a user with all privileges even if it exists grants all privileges on all databases and flushes privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'host' WITH GRANT OPTION;
FLUSH PRIVILEGES;
