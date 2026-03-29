class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p,s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p,s in pair:
            t = (target - p)/s
            print(t)
            if stack and (stack[-1] >= t or t <= 0):
                continue
            else:
                stack.append(t)
        return len(stack)