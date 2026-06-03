-- Write your query below
SELECT u.name, SUM(t.amount) AS balance
FROM users u
left join transactions t on t.account = u.account
group by u.name
HAVING SUM(t.amount) > 10000