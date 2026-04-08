from functools import lru_cache
class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(None)
        def decode(i):
            if i == len(s): return 1
            if s[i] == '0': return 0
            
            # Decision 1: Decode single digit
            res = decode(i + 1)
            
            # Decision 2: Decode two digits (10-26)
            if i + 1 < len(s):
                # Check if it starts with '1' OR starts with '2' and ends 0-6
                if s[i] == '1' or (s[i] == '2' and s[i+1] in "0123456"):
                    res += decode(i + 2)
            return res
            
        return decode(0)