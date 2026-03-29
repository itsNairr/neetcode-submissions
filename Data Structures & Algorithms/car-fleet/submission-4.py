class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        res = 1

        for p, s in pair:
            stack.append((target-p)/s)
        

        prev = None
        for steps in stack:
            if not prev:
                prev = steps
            elif steps > prev:
                res += 1
                prev = steps
        return res
