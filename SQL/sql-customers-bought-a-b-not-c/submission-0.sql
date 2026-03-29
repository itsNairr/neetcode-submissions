-- Write your query below
select c.customer_id, c.customer_name
from customers c
inner join orders o on c.customer_id = o.customer_id
group by c.customer_id
having 
SUM(CASE WHEN o.product_name = 'A' THEN 1 ELSE 0 END) > 0
AND SUM(CASE WHEN o.product_name = 'B' THEN 1 ELSE 0 END) > 0
AND SUM(CASE WHEN o.product_name = 'C' THEN 1 ELSE 0 END) = 0
order by c.customer_name;
