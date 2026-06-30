from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countt = Counter(s1)
        copy = countt.copy()      
        for i, s in enumerate(s2):
            countt = copy.copy()
            if s in countt and countt[s] > 0:
                countt[s] -= 1 
            for j in range(i+1, len(s2)):
                if s2[j] in countt and countt[s2[j]] > 0:
                    countt[s2[j]] -= 1
                elif countt != copy:
                    break
            if not any(countt.values()):
                return True

        return False