-- Script to create table force_name

USE hbtn_0d_2;

-- Create table force_name if it does not exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
