from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        res = 0
        counts = Counter(tasks)
        maxh = list(counts.values())
        heapq.heapify_max(maxh)
        q = deque()
        while maxh or q:
            res += 1

            if not maxh:
                res = q[0][1]
            else:
                cnt = heapq.heappop_max(maxh) - 1
                if cnt:
                    q.append([cnt, res + n])
            if q and q[0][1] == res:
                heapq.heappush_max(maxh, q.popleft()[0])

        return res
            


            
        


        