-- Write your query below
SELECT name
FROM customers c
LEFT JOIN orders o on o.customer_id = c.id
WHERE o.customer_id is NULL