use my_database;
create table employees(
id INT PRIMARY KEY,
emp_name VARCHAR(50),
age INT CHECK (age < 50),
bonus FLOAT DEFAULT 50000.00
);


create table departments(
dept_id INT,
FOREIGN KEY (dept_id) REFERENCES employees(id)
);
SELECT NOW();
SELECT DATE(NOW());
SELECT LENGTH('MYSQL');
SELECT TRIM(' SQL ');
SELECT SUBSTRING('SQL TUTORIAL',5,7);
SELECT ROUND(123.4567,2);
SELECT ABS(-123);



SELECT employees.age,departments.dept_id
FROM employees
JOIN departments
ON employees.age = departments.dept_id;

SELECT 