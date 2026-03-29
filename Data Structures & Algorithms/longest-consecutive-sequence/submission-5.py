class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        sett = sorted(sett)
        ret = []
        prev = None
        highest = 0
        print(sett)
        for num in sett:
            print(num)
            if prev is None or prev == num-1 or prev == num+1:
                ret.append(num)
                print(ret)
            else:
                ret = [num]
                print(ret)
            if highest < len(ret):
                highest = len(ret)
            prev = num
        return highest
        