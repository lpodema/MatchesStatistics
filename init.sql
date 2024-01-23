CREATE DATABASE IF NOT EXISTS Backend;
CREATE USER 'django'@'*' IDENTIFIED BY 'django';
GRANT ALL PRIVILEGES ON mydb.* TO 'django'@'%' IDENTIFIED BY 'django';
GRANT ALL PRIVILEGES ON mydb.* TO 'django'@'localhost' IDENTIFIED BY 'django';