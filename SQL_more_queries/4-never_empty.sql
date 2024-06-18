-- This script creates a table if it does not exist with id deafaulting to 1
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256) NOT NULL
);
