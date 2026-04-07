class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}

        def climb(index):
            if index > len(cost)-1:
                return 0
            if index in cache:
                return cache[index]

            cache[index] = cost[index] + min(climb(index + 1), climb(index + 2))
            return cache[index]
        
        return min(climb(0), climb(1))