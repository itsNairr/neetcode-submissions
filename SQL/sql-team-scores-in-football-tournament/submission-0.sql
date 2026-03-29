-- Write your query below
SELECT team_id, team_name, (
    COALESCE(SUM(CASE WHEN
    (m.host_team = t.team_id AND m.host_goals > m.guest_goals) THEN 3
    WHEN (m.guest_team = t.team_id AND m.host_goals < m.guest_goals) THEN 3
    WHEN (m.host_team = t.team_id AND m.host_goals = m.guest_goals) THEN 1
    WHEN (m.guest_team = t.team_id AND m.host_goals = m.guest_goals) THEN 1
    ELSE 0
    END
    ),0)
) AS num_points
FROM teams t
LEFT JOIN matches m ON m.host_team = t.team_id OR  m.guest_team = t.team_id 
GROUP BY team_id
ORDER BY num_points DESC; 