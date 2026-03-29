class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        unique = set()
        L = 0
        for R in range(len(s)):
            while s[R] in unique:
                unique.remove(s[L])
                L += 1
            length = max(length, R - L + 1)
            unique.add(s[R])
        return length