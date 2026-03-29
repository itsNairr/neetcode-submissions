class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        max_count = 0
        max_length = 0
        left = 0

        for right in range(len(s)):
            # Increment the frequency of the current character
            count[s[right]] += 1
            
            # Get the count of the most frequent character in the current window
            max_count = max(max_count, count[s[right]])
            
            # If the window size minus the most frequent character's count is greater than k, shrink the window
            if (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1
            
            # Update the maximum length of the window
            max_length = max(max_length, right - left + 1)
        
        return max_length