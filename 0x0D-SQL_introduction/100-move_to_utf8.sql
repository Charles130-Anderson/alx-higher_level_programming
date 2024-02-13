-- Task: Convert the 'first_table' in the hbtn_0c_0 database to utf8mb4 character set and utf8mb4_unicode_ci collation.

-- Use the hbtn_0c_0 database
USE `hbtn_0c_0`;

-- Convert the 'first_table' to utf8mb4 character set and utf8mb4_unicode_ci collation
ALTER TABLE `first_table` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
