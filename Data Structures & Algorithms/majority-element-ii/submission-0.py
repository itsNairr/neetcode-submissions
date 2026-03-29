class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        dictt = {}
        for num in nums:
            if num not in dictt:
                dictt[num] = 1
            else:
                dictt[num] += 1

        for key, value in dictt.items():
            if value > len(nums)//3:
                res.append(key)
        return res