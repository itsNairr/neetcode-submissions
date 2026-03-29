class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 1, 0

        n = len(nums)

        while fast != slow:
            print(fast,slow)
            if slow + 1 == n:
                slow = 0
            else:
                slow += 1
            if fast + 2 >= n:
                fast = (fast + 2) - n
            else:
                fast += 1
            
            if nums[slow] == nums[fast]:
                return nums[slow]

