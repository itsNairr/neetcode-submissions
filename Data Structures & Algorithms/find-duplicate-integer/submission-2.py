class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        track = None
        for num in nums:
            if not track or num != track:
                track = num
            else:
                return num