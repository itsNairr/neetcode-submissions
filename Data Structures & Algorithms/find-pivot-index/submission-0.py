class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre = []
        pret, postt = 0, 0
        post = []
        for i in range(len(nums)):
            pret += nums[i]
            postt += nums[(len(nums)-1)-i]
            post.append(postt)
            pre.append(pret)
            i+=1
    
        post.reverse()
        print(pre,post)
        for i in range(len(nums)):
            if pre[i] == post[i]:
                return i
        return -1