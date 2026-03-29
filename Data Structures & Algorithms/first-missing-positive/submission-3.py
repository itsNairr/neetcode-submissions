class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        last = None
        for num in nums:
            if num > 1 and (not last or last < 0):
                return 1
            if last and last >= 0 and num >= 0:
                if num - last >= 2:
                    return last+1
            last = num
        while last < 0:
            last = last+1
        return last+1
        