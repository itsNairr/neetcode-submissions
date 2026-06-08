SELECT o.customer_id, c.name
FROM orders o
LEFT JOIN product p on p.product_id = o.product_id
LEFT JOIN customers c on c.customer_id = o.customer_id
WHERE o.order_date > '2020-05-30' and o.order_date <= '2020-06-30'
GROUP BY o.customer_id, c.name
HAVING SUM(p.price * o.quantity) >= 100

INTERSECT

SELECT o.customer_id, c.name
FROM orders o
LEFT JOIN product p on p.product_id = o.product_id
LEFT JOIN customers c on c.customer_id = o.customer_id
WHERE o.order_date > '2020-06-30' and o.order_date <= '2020-07-31'
GROUP BY o.customer_id, c.name
HAVING SUM(p.price * o.quantity) >= 100