class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s2:
            return False
        l, r, index = 0, 0, 0
        dictt = {}
        while index < len(s2):
            if s2[index] in s1:
                r += 1
                dictt[s2[index]] = dictt.get(s2[index], 0) + 1
                while dictt[s2[index]] > s1.count(s2[index]):
                    dictt[s2[l]] -= 1
                    if dictt[s2[l]] == 0:
                        del dictt[s2[l]]
                    l += 1
            else:
                dictt.clear()
                l, r = index + 1, index + 1
            
            if all(dictt.get(char, 0) == s1.count(char) for char in set(s1)) and r - l == len(s1):
                return True
            index += 1
        
        return False


                