## SQL Intermediate Topics – Hinglish Short Notes + Interview Q&A

### 1. **Aggregate Functions (SUM, AVG, COUNT, GROUP BY, HAVING)**
- **COUNT, SUM, AVG**: Data ka total, average, ya count nikalne ke liye.
- **GROUP BY**: Data ko group karne ke liye (jaise department wise).
- **HAVING**: Grouped data pe filter lagane ke liye (jaise sirf un departments jinka avg salary > 50k).

### 2. **Joins (INNER, LEFT, RIGHT, FULL, SELF)**
- **INNER JOIN**: Dono tables me matching rows.
- **LEFT JOIN**: Left table ke saare, right ke matching.
- **RIGHT JOIN**: Right table ke saare, left ke matching.
- **FULL OUTER JOIN**: Dono tables ke saare rows (matching + non-matching).
- **SELF JOIN**: Table ko khud se join karna (jaise employee-manager).

### 3. **Data Combination (UNION, INTERSECT, EXCEPT)**
- **UNION**: 2 queries ka result combine karta hai, duplicates hata ke.
- **UNION ALL**: Combine karta hai, duplicates bhi rakhta hai.
- **INTERSECT**: Dono queries me common rows.
- **EXCEPT**: Pehli query me hai, dusri me nahi.

### 4. **Subqueries & Nested Aggregation**
- Query ke andar query likhna (jaise max, min, avg nikalne ke liye).

***

## Interview Questions + Answers (with Concepts)

### 1. Har department me kitne employees hain aur unka avg salary kya hai?
```sql
SELECT d.department_name, 
       COUNT(e.employee_id) as employee_count,
       AVG(e.salary) as avg_salary
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_id, d.department_name;
```
**Concepts:** LEFT JOIN, GROUP BY, COUNT, AVG

***

### 2. Sirf un departments ko dikhao jinka avg salary 50,000 se zyada hai
```sql
SELECT department_id, AVG(salary) as avg_salary
FROM employees
GROUP BY department_id
HAVING AVG(salary) > 50000;
```
**Concepts:** GROUP BY, HAVING, AVG

***

### 3. Sabse zyada total salary wala department kaun sa hai?
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
**Concepts:** GROUP BY, SUM, Subquery, MAX, HAVING

***

### 4. Employee ka naam aur unka department ka naam dikhao (INNER JOIN)
```sql
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id;
```
**Concepts:** INNER JOIN

***

### 5. Saare departments dikhao, chahe employee ho ya na ho (LEFT JOIN)
```sql
SELECT d.department_name, e.first_name, e.last_name
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id;
```
**Concepts:** LEFT JOIN

***

### 6. Employee aur unke manager ka naam dikhao (SELF JOIN)
```sql
SELECT e1.first_name || ' ' || e1.last_name as Employee,
       e2.first_name || ' ' || e2.last_name as Manager
FROM employees e1
LEFT JOIN employees e2 ON e1.manager_id = e2.employee_id;
```
**Concepts:** SELF JOIN, String Concatenation

***

### 7. Har customer ke orders dikhao (FULL OUTER JOIN)
```sql
SELECT c.customer_name, o.order_id, o.order_date
FROM customers c
FULL OUTER JOIN orders o ON c.customer_id = o.customer_id;
```
**Concepts:** FULL OUTER JOIN

***

### 8. Order details ke saath product ka naam dikhao (JOIN on multiple columns)
```sql
SELECT od.order_id, p.product_name, od.quantity, od.unit_price
FROM order_details od
INNER JOIN products p ON od.product_id = p.product_id;
```
**Concepts:** INNER JOIN, Multiple Tables

***

### 9. Employee aur customer ke emails combine karo (UNION)
```sql
SELECT email as contact_email, 'Employee' as type
FROM employees
WHERE email IS NOT NULL
UNION
SELECT email as contact_email, 'Customer' as type
FROM customers
WHERE email IS NOT NULL;
```
**Concepts:** UNION

***

### 10. UNION vs UNION ALL ka difference?
- **UNION**: Duplicates hata deta hai, result sorted hota hai.
- **UNION ALL**: Duplicates bhi rakhta hai, result sorted nahi hota (fast hota hai).

***

### 11. Kaunse cities me customer aur employee dono hain? (INTERSECT)
```sql
SELECT city FROM customers
INTERSECT
SELECT city FROM employees;
```
**Concepts:** INTERSECT

***

### 12. Top 3 customers jinhone sabse zyada order amount diya hai
```sql
SELECT c.customer_name, SUM(o.order_amount) as total_spent
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name
ORDER BY total_spent DESC
LIMIT 3;
```
**Concepts:** INNER JOIN, GROUP BY, SUM, ORDER BY, LIMIT

***

### 13. Wo employees jinka salary unke department ke avg salary se zyada hai
```sql
SELECT e.first_name, e.last_name, e.salary, e.department_id
FROM employees e
WHERE e.salary > (
    SELECT AVG(salary)
    FROM employees e2
    WHERE e2.department_id = e.department_id
);
```
**Concepts:** Subquery, AVG, WHERE

***

### 14. Wo departments jisme 5 se zyada employees hain aur avg salary 45,000 se zyada hai
```sql
SELECT d.department_name, COUNT(e.employee_id) as emp_count, AVG(e.salary) as avg_salary
FROM departments d
INNER JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_id, d.department_name
HAVING COUNT(e.employee_id) > 5 AND AVG(e.salary) > 45000;
```
**Concepts:** INNER JOIN, GROUP BY, HAVING, COUNT, AVG

***

### 15. Har order me order_date aur ship_date ka difference (days me)
```sql
SELECT order_id, order_date, ship_date,
       DATEDIFF(day, order_date, ship_date) as days_to_ship
FROM orders
WHERE ship_date IS NOT NULL;
```
**Concepts:** DATEDIFF, WHERE

***

## Extra Coding Round Questions (with Answers)

### 16. Har department ka max salary aur us employee ka naam dikhao
```sql
SELECT d.department_name, e.first_name, e.last_name, e.salary
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id
WHERE (e.department_id, e.salary) IN (
    SELECT department_id, MAX(salary)
    FROM employees
    GROUP BY department_id
);
```
**Concepts:** INNER JOIN, GROUP BY, MAX, Tuple Filtering

***

### 17. Kaunse employees ne kabhi order process kiya hai? (orders table se)
```sql
SELECT DISTINCT e.first_name, e.last_name
FROM employees e
INNER JOIN orders o ON e.employee_id = o.employee_id;
```
**Concepts:** INNER JOIN, DISTINCT

***

### 18. Har product ka total quantity kitna order hua hai?
```sql
SELECT p.product_name, SUM(od.quantity) as total_qty
FROM products p
INNER JOIN order_details od ON p.product_id = od.product_id
GROUP BY p.product_id, p.product_name;
```
**Concepts:** INNER JOIN, GROUP BY, SUM

***

### 19. Kaunse customers ne kabhi order nahi diya?
```sql
SELECT c.customer_name
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;
```
**Concepts:** LEFT JOIN, WHERE IS NULL

***

### 20. Har department me kitne managers hain (manager_id NULL nahi ho)?
```sql
SELECT department_id, COUNT(DISTINCT manager_id) as manager_count
FROM employees
WHERE manager_id IS NOT NULL
GROUP BY department_id;
```
**Concepts:** GROUP BY, COUNT DISTINCT, WHERE

***

**Tip:**
- Interview me pehle table ka structure samajh, fir question ko breakdown kar, aur concept yaad rakh ke query likh.
- Joins, Aggregation, Subquery, Filtering, Grouping – yeh sab repeat hote hain!
- Practice karte reh, khud se queries likh, aur revise karte reh yeh short notes!

**Best of luck!**
