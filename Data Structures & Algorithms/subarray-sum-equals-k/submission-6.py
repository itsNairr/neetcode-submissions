class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = curSum = 0
        prefixes = { 0:1 }
        for num in nums:
            curSum += num
            prevSum = curSum - k
            res += prefixes.get(prevSum, 0)
            prefixes[curSum] = prefixes.get(curSum, 0) + 1
        return res