class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        res = 1

        prev = None
        for p, s in pair:
            steps = (target-p)/s
            if not prev:
                prev = steps
            elif steps > prev:
                res += 1
                prev = steps
        return res
