class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numss = sorted(list(set(nums)))
        print(numss)
        maxx = 0
        temp = 0
        prevnum = None
        for num in numss:
            if not prevnum and prevnum is not 0 or abs(num - prevnum) == 1:
                temp += 1
                print(num)
                print(prevnum)
                print(temp)
                if temp > maxx:
                    maxx = temp
                prevnum = num
            else:
                temp = 1
                print(num)
                print(prevnum)
                print(temp)
                prevnum = num
        return maxx