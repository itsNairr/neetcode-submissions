from functools import lru_cache
class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(None)
        def decode(index):
            if index == len(s):
                return 1
            if s[index] == '0':
                return 0
            res = decode(index + 1)
            if index + 1 < len(s):
                two_digit = int(s[index : index + 2])
                if 10 <= two_digit <= 26:
                    res += decode(index + 2)
            return res
        return decode(0)
