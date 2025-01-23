--create our database if it does not exist--
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

--create a new user in  the localhost with all privileges--
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

--grant all privileges to the user in the database--
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

--Grant all Select privileges on the performance_schema database to the user--
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';