-- Write your query below
SELECT c1.seat_id
FROM cinema c1
WHERE free = 1 and ((SELECT c2.free from cinema c2 where c2.seat_id = c1.seat_id + 1) = 1 or (SELECT c2.free from cinema c2 where c2.seat_id = c1.seat_id - 1) = 1)