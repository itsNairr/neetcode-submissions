class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = s.replace(" ", "")
        new = "".join(filter(str.isalnum, temp)).lower()
        reverse = new[::-1]
        return reverse == new