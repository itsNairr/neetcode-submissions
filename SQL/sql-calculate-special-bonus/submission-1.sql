-- Write your query below
select employee_id, 
    CASE
        WHEN name NOT LIKE 'M%' and employee_id%2 = 1 THEN salary
        ELSE 0
    END AS bonus
from employees
order by employee_id asc;