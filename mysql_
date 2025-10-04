-- Employees Table

use interview
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    hire_date DATE,
    salary DECIMAL(10,2),
    department_id INT,
    manager_id INT
);

-- Departments Table
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100),
    location VARCHAR(100)
);

-- Orders Table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    ship_date DATE,
    order_amount DECIMAL(10,2),
    employee_id INT
);

-- Customers Table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    city VARCHAR(50),
    country VARCHAR(50)
);

-- Products Table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2)
);

-- Order_Details Table
CREATE TABLE order_details (
    order_id INT,
    product_id INT,
    quantity INT,
    unit_price DECIMAL(10,2)
);
-- Departments


INSERT INTO departments VALUES
(1, 'Engineering', 'Bangalore'),
(2, 'Finance', 'Mumbai'),
(3, 'Sales', 'Delhi'),
(4, 'HR', 'Bangalore');

-- Employees
INSERT INTO employees VALUES
(101, 'Anil', 'Sharma', 'anil.sharma@example.com', '2022-03-15', 70000, 1, 201),
(102, 'Beena', 'Menon', 'beena.menon@example.com', '2023-08-07', 52000, 2, 202),
(103, 'Chetan', 'Desai', 'chetan.desai@example.com', '2021-01-12', 48000, 2, 202),
(104, 'Deepa', 'Kaur', 'deepa.kaur@example.com', '2022-11-23', 54000, 4, 201),
(105, 'Ekta', 'Patel', 'ekta.patel@example.com', '2021-06-30', 39000, 3, 203),
(201, 'Gopal', 'Nair', 'gopal.nair@example.com', '2020-07-15', 95000, 1, NULL),
(202, 'Harsha', 'Roy', 'harsha.roy@example.com', '2019-04-18', 81000, 2, NULL),
(203, 'Imran', 'Khan', 'imran.khan@example.com', '2018-12-01', 86000, 3, NULL);

-- Customers
INSERT INTO customers VALUES
(1, 'Suresh Traders', 'Nagpur', 'India'),
(2, 'Mehta Co', 'Mumbai', 'India'),
(3, 'Orbit LLC', 'Hyderabad', 'India'),
(4, 'Zenith Global', 'Bangalore', 'India');

-- Orders
INSERT INTO orders VALUES
(1001, 1, '2023-07-01', '2023-07-03', 1100, 102),
(1002, 2, '2023-07-02', '2023-07-05', 2500, 101),
(1003, 2, '2023-08-14', '2023-08-16', 1950, 101),
(1004, 3, '2023-08-17', '2023-08-20', 500, 105),
(1005, 4, '2023-09-01', NULL, 1800, 103);

-- Products
INSERT INTO products VALUES
(10, 'Laptop', 'Electronics', 900),
(11, 'Tablet', 'Electronics', 400),
(12, 'Desk Chair', 'Furniture', 100),
(13, 'Monitor', 'Electronics', 300),
(14, 'Pen Pack', 'Stationery', 20);

-- Order_Details
INSERT INTO order_details VALUES
(1001, 10, 1, 900),
(1001, 12, 2, 100),
(1002, 11, 5, 400),
(1002, 14, 5, 20),
(1003, 13, 2, 300),
(1004, 14, 25, 20),
(1005, 10, 2, 900);

## Practice Database Schema
## Interview Questions with Answers
### Aggregate Functions

-- **Q1: Write a query to find the total number of employees in each department and their average salary.**


SELECT d.department_name, 
       COUNT(e.employee_id) as employee_count,
       AVG(e.salary) as avg_salary
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_id, d.department_name;


**Q2: Find departments where the average salary is greater than $50,000.**

```sql
SELECT department_id, AVG(salary) as avg_salary
FROM employees
GROUP BY department_id
HAVING AVG(salary) > 50000;
```

**Q3: Write a nested aggregation query to find the department with the highest total salary.**

```sql
SELECT department_id, SUM(salary) as total_salary
FROM employees
GROUP BY department_id
HAVING SUM(salary) = (
    SELECT MAX(dept_total) 
    FROM (
        SELECT SUM(salary) as dept_total 
        FROM employees 
        GROUP BY department_id
    ) subquery
);
```

### Table Relationships and Joins

**Q4: Write an INNER JOIN to get employee names with their department names.**

```sql
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id;
```

**Q5: Use LEFT JOIN to show all departments and their employees, including departments with no employees.**

```sql
SELECT d.department_name, e.first_name, e.last_name
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id;
```

**Q6: Write a SELF JOIN to find employees and their managers.**

```sql
SELECT e1.first_name + ' ' + e1.last_name as Employee,
       e2.first_name + ' ' + e2.last_name as Manager
FROM employees e1
LEFT JOIN employees e2 ON e1.manager_id = e2.employee_id;
```

**Q7: Find all customers and their orders using FULL OUTER JOIN.**

```sql
SELECT c.customer_name, o.order_id, o.order_date
FROM customers c
FULL OUTER JOIN orders o ON c.customer_id = o.customer_id;
```

**Q8: Join on multiple columns to get order details with product information.**

```sql
SELECT od.order_id, p.product_name, od.quantity, od.unit_price
FROM order_details od
INNER JOIN products p ON od.product_id = p.product_id;
```

### Data Combination

**Q9: Use UNION to combine employee emails and customer emails.**

```sql
SELECT email as contact_email, 'Employee' as type
FROM employees
WHERE email IS NOT NULL
UNION
SELECT email as contact_email, 'Customer' as type
FROM customers
WHERE email IS NOT NULL;
```

**Q10: What's the difference between UNION and UNION ALL?**

**Answer:** UNION removes duplicate records and sorts the result, while UNION ALL includes all records including duplicates and doesn't sort. UNION ALL is faster since it doesn't need to check for duplicates.[1][2]

```sql
-- UNION (removes duplicates)
SELECT city FROM customers
UNION
SELECT city FROM employees;

-- UNION ALL (keeps duplicates)
SELECT city FROM customers
UNION ALL
SELECT city FROM employees;
```

**Q11: Use INTERSECT to find cities that have both customers and employees.**

```sql
SELECT city FROM customers
INTERSECT
SELECT city FROM employees;
```

### Complex Intermediate Questions

**Q12: Find the top 3 customers with the highest total order amounts.**

```sql
SELECT c.customer_name, SUM(o.order_amount) as total_spent
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name
ORDER BY total_spent DESC
LIMIT 3;
```

**Q13: Find employees whose salary is above the average salary in their department.**

```sql
SELECT e.first_name, e.last_name, e.salary, e.department_id
FROM employees e
WHERE e.salary > (
    SELECT AVG(salary)
    FROM employees e2
    WHERE e2.department_id = e.department_id
);
```

**Q14: Write a query to find departments with more than 5 employees and their average salary is above $45,000.**

```sql
SELECT d.department_name, COUNT(e.employee_id) as emp_count, AVG(e.salary) as avg_salary
FROM departments d
INNER JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_id, d.department_name
HAVING COUNT(e.employee_id) > 5 AND AVG(e.salary) > 45000;
```

**Q15: Find the difference in days between order date and ship date for each order.**

```sql
SELECT order_id, order_date, ship_date,
       DATEDIFF(day, order_date, ship_date) as days_to_ship
FROM orders
WHERE ship_date IS NOT NULL;
```

This comprehensive setup allows practice of all intermediate SQL concepts including aggregate functions, various types of joins, data combination operations, and complex queries that are commonly asked in interviews. The database schema is designed to interconnect multiple tables, enabling realistic practice scenarios that mirror real-world database structures.[2][4][1]

[1](https://upesonline.ac.in/blog/advanced-sql-interview-questions)
[2](https://codesignal.com/blog/interview-prep/28-sql-interview-questions-and-answers-from-beginner-to-senior-level/)
[3](https://www.interviewbit.com/sql-interview-questions/)
[4](https://www.geeksforgeeks.org/sql/sql-interview-questions/)
[5](https://www.youtube.com/watch?v=oX5Y26O5dBE)
[6](https://datalemur.com/blog/advanced-sql-interview-questions)
[7](https://roadmap.sh/questions/sql-queries)



