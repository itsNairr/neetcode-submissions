class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L, length = 0, 0
        counts = {}
        for R in range(len(s)):
            counts[s[R]] = counts.get(s[R], 0) + 1
            while R - L + 1 - max(counts.values()) > k:
                counts[s[L]] -= 1
                L += 1
            length = max(length, R-L +1)
        return length