SELECT c.name as country
FROM calls cs
LEFT JOIN person p ON p.id = cs.caller_id or p.id = cs.callee_id
LEFT JOIN country c ON c.country_code = left(p.phone_number, 3)
GROUP BY c.name
HAVING SUM(duration)/COUNT(duration) > (SELECT SUM(duration)/COUNT(duration) FROM calls)
