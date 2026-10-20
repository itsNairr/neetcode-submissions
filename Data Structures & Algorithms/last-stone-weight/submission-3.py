import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            first = heapq.heappop_max(stones)
            second = heapq.heappop_max(stones)

            tot = abs(first - second)
            if tot:
                heapq.heappush_max(stones, tot)


        return stones[0] if len(stones) > 0 else 0

