class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        cache = {}
        def execute(index, total):
            state = (index, total)
            if total == 0:
                return 0
            if index > len(coins)-1:
                return float('inf')
            if state in cache:
                return cache[state]
            if total >= coins[index]:
                cache[(index, total)] = min(1 + execute(index, total-coins[index]), execute(index+1, total))
            else:
                cache[(index, total)] = execute(index+1, total)
            return cache[(index, total)]
        final = execute(0, amount)
        return final if final < float('inf') else -1