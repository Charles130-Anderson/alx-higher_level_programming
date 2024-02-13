-- Task: Convert all tables in the hbtn_0c_0 database to utf8mb4 character set and utf8mb4_unicode_ci collation.

-- Select the database to work with
USE `hbtn_0c_0`;

-- Get a list of all tables in the current database
SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = DATABASE();

-- Iterate over each table and convert its character set and collation
-- Note: This part must be executed manually for each table returned by the SELECT statement above
-- ALTER TABLE `table_name` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
