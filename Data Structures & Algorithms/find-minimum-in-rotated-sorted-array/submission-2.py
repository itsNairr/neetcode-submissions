class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        mid = 0
        res = float('inf')
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid - 1
            res = min(res, nums[mid])

        return res
