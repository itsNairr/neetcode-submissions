-- Write your query below
SELECT w.name AS warehouse_name, SUM((p.width * p.length * p.height) * w.units) AS volume
FROM warehouse w
LEFT JOIN products p ON p.product_id = w.product_id
GROUP BY warehouse_name