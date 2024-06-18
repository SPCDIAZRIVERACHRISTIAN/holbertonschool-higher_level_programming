-- This script creates a table if it does'nt exist with a unique id defaulting to 1

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
