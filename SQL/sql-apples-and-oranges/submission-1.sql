-- Write your query below
SELECT sale_date, SUM(CASE WHEN fruit = 'apples' then sold_num else 0 end) - SUM(CASE WHEN fruit = 'oranges' then sold_num else 0 end) as diff
from sales
group by sale_date;