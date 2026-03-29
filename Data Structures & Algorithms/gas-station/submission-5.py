class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        tank = 0
        i = 0
        mi = 0
        for g,c in zip(gas,cost):
            tank += g - c
            if tank < 0:
                tank = 0
                mi = i + 1
            i += 1
        return mi