-- Write your query below
SELECT u.name, (
    CASE WHEN SUM(r.distance) is NULL THEN 0 ELSE SUM(r.distance) END) as travelled_distance
FROM users u
LEFT JOIN rides r on u.id = r.user_id
GROUP BY u.name
ORDER BY travelled_distance DESC