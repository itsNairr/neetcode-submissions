class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        filtered_chars = []

        for char in s:
            if char.isalnum():  # Check if the character is alphanumeric
                filtered_chars.append(char)

        filtered_s = ''.join(filtered_chars)
        return filtered_s == filtered_s[::-1]