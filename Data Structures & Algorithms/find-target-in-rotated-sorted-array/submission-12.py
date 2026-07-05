class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
            print(nums[mid])
            if nums[mid] == target:
                return mid
            if nums[mid] <= nums[high]:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[mid] > target >= nums[low]:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1
