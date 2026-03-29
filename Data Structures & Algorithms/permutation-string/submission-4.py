class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s2:
            return False
        l, r, index = 0,0,0
        dictt = {}
        while index < len(s2):
            if s2[index] in s1:
                r+=1
                if s2[index] not in dictt or dictt[s2[index]] < s1.count(s2[index]):
                    dictt[s2[index]] = dictt.get(s2[index], 0) + 1
                else:
                    dictt[s2[index]] += 1
                    while dictt.get(s2[l]) != s1.count(s2[index]):
                        dictt[s2[l]] -= 1
                        l+=1
            else:
                while l != r+1:
                    if s2[l] in dictt:
                        dictt[s2[l]] -= 1
                    l+=1
                r+=1
            if all(value == s1.count(key) for key, value in dictt.items()) and len(dictt) == len(''.join(set(s1))):
                return True
            index +=1
        print(dictt)
        print(l, r)
        return False

                