class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        res = 0
        for n in sett:
            if n-1 not in sett:
                curr = 1

                while n + curr in sett:
                    curr += 1
            
                res = max(res, curr)

        return res


