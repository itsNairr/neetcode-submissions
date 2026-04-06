class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            l, r = i, i
            while 0 <= l <= len(s)-1 and 0 <= r <= len(s)-1 and s[r] == s[l]:
                count += 1
                r += 1
                l -= 1
            l, r = i, i + 1
            while 0 <= l <= len(s)-1 and 0 <= r <= len(s)-1 and s[r] == s[l]:
                count += 1
                r += 1
                l -= 1
        return count