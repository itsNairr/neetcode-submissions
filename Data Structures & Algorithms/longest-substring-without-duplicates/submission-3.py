class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = set()
        maxx = 0
        left = 0

        for right in range(len(s)):
            while s[right] in ss:
                ss.remove(s[left])
                left += 1

            ss.add(s[right])

            maxx = max(maxx, right - left + 1)
        
        return maxx
        