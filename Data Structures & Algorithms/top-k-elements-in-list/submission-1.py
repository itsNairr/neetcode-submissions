class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictt = {}
        ret = []
        for num in nums:
            if num not in dictt:
                dictt[num] =  1
            else:
                dictt[num] += 1
        for _ in range(k):
            key = max(dictt, key=dictt.get)
            ret.append(key)
            dictt.pop(key)
        return ret

            