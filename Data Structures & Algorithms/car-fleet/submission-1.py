class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = dict(zip(position, speed))
        sorted_dict = dict(sorted(pair.items(), reverse=True))
        stack = []
        for p, s in sorted_dict.items():
            stack.append((target - p) / s)
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
