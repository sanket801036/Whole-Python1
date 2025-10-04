-- Employees Table
```sql
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

```
## Practice Database Schema
## Interview Questions with Answers
### Aggregate Functions

-- **Q1: Write a query to find the total number of employees in each department and their average salary.**

```sql
SELECT d.department_name, 
       COUNT(e.employee_id) as employee_count,
       AVG(e.salary) as avg_salary
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_id, d.department_name;
```

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

Below are the answers for each question along with which concepts are used. Notes are in Hinglish for revision ease.

***

1. **Show the youngest and oldest student's details**
```sql
SELECT * FROM students WHERE age = (SELECT MIN(age) FROM students)
UNION
SELECT * FROM students WHERE age = (SELECT MAX(age) FROM students);
```
*Concepts: MIN/MAX (Aggregate), Subquery, UNION*

***

2. **Count of students in each city**
```sql
SELECT city, COUNT(*) AS student_count
FROM students
GROUP BY city;
```
*Concepts: GROUP BY, COUNT (Aggregation)*

***

3. **Students not from 'Mumbai' and not from 'Delhi'**
```sql
SELECT * FROM students
WHERE city NOT IN ('Mumbai', 'Delhi');
```
*Concepts: WHERE, NOT IN (Filtering)*

***

4. **Students with no fees or fees below average**
```sql
SELECT * FROM students
WHERE fees IS NULL
   OR fees < (SELECT AVG(fees) FROM students);
```
*Concepts: WHERE, IS NULL, Subquery, AVG (Aggregate)*

***

5. **City not null & name starts with 'A'**
```sql
SELECT * FROM students
WHERE city IS NOT NULL AND first_name LIKE 'A%';
```
*Concepts: WHERE, IS NOT NULL, LIKE (Pattern Matching)*

***

6. **Top 3 oldest students; show full names & ages**
```sql
SELECT CONCAT(first_name, ' ', last_name) AS full_name, age
FROM students
ORDER BY age DESC
LIMIT 3;
```
*Concepts: ORDER BY, DESC, LIMIT, CONCAT (String)*

***

7. **Sort by grade descending, then age ascending**
```sql
SELECT * FROM students
ORDER BY grade DESC, age ASC;
```
*Concepts: ORDER BY, Multiple Columns, DESC/ASC (Sorting)*

***

8. **Two cities with most students**
```sql
SELECT city, COUNT(*) AS student_count
FROM students
GROUP BY city
ORDER BY student_count DESC
LIMIT 2;
```
*Concepts: GROUP BY, COUNT, ORDER BY, LIMIT*

***

9. **Last names with exactly five letters**
```sql
SELECT * FROM students
WHERE LENGTH(last_name) = 5;
-- OR
SELECT * FROM students
WHERE last_name LIKE '_____';
```
*Concepts: LENGTH/String Functions, LIKE (Pattern Matching)*

***

10. **First name with 'e' as second letter**
```sql
SELECT * FROM students
WHERE first_name LIKE '_e%';
```
*Concepts: LIKE (Pattern Matching)*

***

11. **Cities starting with 'B', 'P', or 'D'**
```sql
SELECT * FROM students
WHERE city LIKE 'B%' OR city LIKE 'P%' OR city LIKE 'D%';
```
*Concepts: WHERE, LIKE (Multiple Patterns)*

***

12. **Students grade not 'A' or 'C'**
```sql
SELECT * FROM students
WHERE grade NOT IN ('A', 'C');
```
*Concepts: WHERE, NOT IN (Filtering)*

***

13. **Ages 18-21 excluding grade 'B'**
```sql
SELECT * FROM students
WHERE age BETWEEN 18 AND 21 AND grade <> 'B';
```
*Concepts: BETWEEN, AND, <> (Filtering)*

***

14. **NULL in city OR fees**
```sql
SELECT * FROM students
WHERE city IS NULL OR fees IS NULL;
```
*Concepts: WHERE, IS NULL*

***

15. **Fees not null, multiple of 5000 or max fee**
```sql
SELECT * FROM students
WHERE fees IS NOT NULL
  AND (fees % 5000 = 0 OR fees = (SELECT MAX(fees) FROM students));
```
*Concepts: Modulo (%), Subquery, MAX, IS NOT NULL*

***

16. **First name = last name**
```sql
SELECT * FROM students
WHERE first_name = last_name;
```
*Concepts: WHERE, Comparison/String Functions*

***

17. **Students in each grade including zero count**
```sql
SELECT g.grade, COUNT(s.student_id) AS student_count
FROM (SELECT DISTINCT grade FROM students) g
LEFT JOIN students s ON g.grade = s.grade
GROUP BY g.grade;
```
*Concepts: LEFT JOIN, GROUP BY, COUNT, Subquery*

***

18. **Sum and avg fees per city**
```sql
SELECT city, SUM(fees) AS total_fees, AVG(fees) AS avg_fees
FROM students
GROUP BY city;
```
*Concepts: GROUP BY, SUM, AVG*

***

19. **City(s) with largest average fee**
```sql
SELECT city
FROM students
GROUP BY city
HAVING AVG(fees) = (
    SELECT MAX(avg_fees) FROM (
        SELECT AVG(fees) AS avg_fees FROM students GROUP BY city
    ) x
);
```
*Concepts: GROUP BY, HAVING, Nested Subquery, MAX, AVG*

***

20. **Grade with smallest total fees**
```sql
SELECT grade
FROM students
GROUP BY grade
HAVING SUM(fees) = (
    SELECT MIN(total_fees) FROM (
        SELECT SUM(fees) AS total_fees
        FROM students
        GROUP BY grade
    ) y
);
```
*Concepts: GROUP BY, HAVING, SUM, MIN, Subquery*

***

21. **Names with no vowels (a, e, i, o, u)**
```sql
SELECT * FROM students
WHERE CONCAT(first_name, last_name) NOT LIKE '%a%'
  AND CONCAT(first_name, last_name) NOT LIKE '%e%'
  AND CONCAT(first_name, last_name) NOT LIKE '%i%'
  AND CONCAT(first_name, last_name) NOT LIKE '%o%'
  AND CONCAT(first_name, last_name) NOT LIKE '%u%';
```
*Concepts: WHERE, CONCAT, NOT LIKE (Multiple Patterns)*

***

22. **Cities with more than one student**
```sql
SELECT * FROM students
WHERE city IN (
    SELECT city FROM students GROUP BY city HAVING COUNT(*) > 1
);
```
*Concepts: IN, GROUP BY, HAVING*

***

23. **Students sharing both grade and age**
```sql
SELECT * FROM students s1
WHERE EXISTS (
    SELECT 1 FROM students s2
    WHERE s1.student_id <> s2.student_id
      AND s1.grade = s2.grade
      AND s1.age = s2.age
);
```
*Concepts: EXISTS, Self-Join/Correlated Subquery*

***

24. **For each grade, highest fee & student name(s)**
```sql
SELECT grade,
       fees AS max_fee,
       CONCAT(first_name, ' ', last_name) AS full_name
FROM students
WHERE (grade, fees) IN (
    SELECT grade, MAX(fees) FROM students GROUP BY grade
);
```
*Concepts: GROUP BY, MAX, Tuple Filtering, CONCAT*

***

25. **All students in one comma-separated row**
```sql
SELECT GROUP_CONCAT(CONCAT(first_name, ' ', last_name)) AS all_students
FROM students;
-- (Syntax may change: MySQL uses GROUP_CONCAT, others STRING_AGG or LISTAGG)
```
*Concepts: Aggregate function, String functions*

***

**Notes:**  
- Har query ke aage concept likha hua hai – revise karte time point-wise yaad rakhna.  
- Subquery, Aggregation, Joins, Filtering, Pattern Matching – yeh sab interview me repeat hote hain!
- Practice/modify queries khud se bhi kar sakte ho taaki syntax confidence aaye.

**Best of luck! Coding interview crack karne ke liye yeh notes + queries ka use regular revision ke liye karo!**

