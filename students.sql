CREATE DATABASE student_db;
USE student_db;

CREATE USER 'root'@'localhost' IDENTIFIED BY '#Chowdary@536';
GRANT ALL PRIVILEGES ON student_db.* TO 'root'@'localhost';
FLUSH PRIVILEGES;

select * from students;

