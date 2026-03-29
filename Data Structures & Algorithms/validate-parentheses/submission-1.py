class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        s1 = {'(': 0, '[': 1, '{': 2}
        s2 = {')': '(', ']': '[', '}': '{'}
        stack = []
        for p in s:
            if p in s1:
                stack.append(p)
            elif p in s2:
                if len(stack) == 0 or stack.pop() != s2[p]:
                    return False
        return len(stack) == 0

        