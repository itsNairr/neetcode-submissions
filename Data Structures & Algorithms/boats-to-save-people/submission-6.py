class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res, l, r = 0, 0, len(people) - 1
        copy = limit
        while l <= r:
            copy = limit - people[r]
            r -= 1
            if copy >= people[l]:
                copy -= people[l]
                l += 1
            res += 1

        return res