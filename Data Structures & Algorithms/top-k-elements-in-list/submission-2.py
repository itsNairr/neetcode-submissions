class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictt = {}
        res = []
        for num in nums:
            if num not in dictt.keys():
                dictt[num] = 1
            else:
                dictt[num] += 1
        sorted_items_desc = sorted(dictt.items(), key=lambda item: item[1], reverse=True)
        # Convert back to a dictionary
        sorted_dict_desc = dict(sorted_items_desc)
        return list(sorted_dict_desc.keys())[:k]
