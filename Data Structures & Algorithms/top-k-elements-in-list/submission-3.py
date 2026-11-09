from collections import Counter
from operator import itemgetter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sorted_dict = dict(sorted(count.items(), key=itemgetter(1), reverse=True))
        return list(sorted_dict.keys())[:k]

