-- Write your query below


SELECT DISTINCT l.page_id as recommended_page
FROM likes l
LEFT JOIN friendship f ON l.user_id = f.user1_id or l.user_id = f.user2_id
WHERE (user1_id = 1 or user2_id = 1) and l.user_id != 1 and l.page_id not in (
    SELECT l2.page_id
    FROM likes l2
    WHERE l2.user_id = 1
)