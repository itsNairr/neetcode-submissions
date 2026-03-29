class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j <= min(len(res)-1, len(strs[i])-1)  and res[j] == strs[i][j]:
                j+=1
            res = res[:j]
        return res