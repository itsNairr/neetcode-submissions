class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)
        res = []
        print(nums_sorted)
        for index, num in enumerate(nums_sorted):
            right = len(nums)-1
            left = index + 1
            while left < right:
                target = num + nums_sorted[left] + nums_sorted[right]
                if target < 0:
                    left += 1
                elif target == 0:
                    if [num, nums_sorted[left], nums_sorted[right]] not in res:
                        res.append([num, nums_sorted[left], nums_sorted[right]])
                    left += 1
                else:
                    right -= 1
        return res
                