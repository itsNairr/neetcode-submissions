class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums)-1
        def binary_search(L, R):
            mid = L + (R - L) // 2
            print(mid)
            if L > R:
                return -1
            if target < nums[mid]:
                return binary_search(L, mid-1)
            if target > nums[mid]:
                return binary_search(mid+1, R)
            else:
                return mid
        return binary_search(L, R)