class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        print(pair)
        stack = []
        for p, s in pair:
            t = (target - p)/s
            print(t)
            if not stack:
                stack.append(t)
            if stack[-1] < t:
                stack.append(t)
        return len(stack)