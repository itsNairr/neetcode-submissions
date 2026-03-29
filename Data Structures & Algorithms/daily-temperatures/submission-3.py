class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for index, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                top = stack.pop()
                res[top] = index - top
            stack.append(index)
        return res