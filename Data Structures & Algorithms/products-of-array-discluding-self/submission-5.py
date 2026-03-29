class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post, prt, pot = [], deque(), 1, 1
        res = []
        for i in range(len(nums)):
            prt *=nums[i]
            pot *=nums[len(nums)-1-i]
            pre.append(prt)
            post.appendleft(pot)

        for i in range(len(nums)):
            if 0 < i < len(nums)-1:
                res.append(pre[i-1]*post[i+1])
            elif i == 0:
                res.append(post[i+1])
            else:
                res.append(pre[i-1])


        return res

            
            