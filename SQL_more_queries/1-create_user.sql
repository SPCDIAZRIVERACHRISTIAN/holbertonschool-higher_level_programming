-- This script creates a user with all privileges even if it exists grants all privileges on/
-- *.* to 'user_0d_1' @ 'localhost' identified by 'user_0d_1_pwd' with grant option;
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
