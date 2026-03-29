from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()  # Stores indices
        l = r = 0

        while r < len(nums):
            # 1. Maintain Monotonic Property
            # Remove smaller values from the back; they are useless now.
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # 2. Evict indices that have fallen out of the window
            if l > q[0]:
                q.popleft()

            # 3. Add to result once the window reaches size k
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
            
        return res