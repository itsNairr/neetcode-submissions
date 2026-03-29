class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ss = set()
        for num in nums:
            if num in ss:
                return num
            else:
                ss.add(num)

        return 0
        