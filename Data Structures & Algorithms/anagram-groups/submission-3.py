class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return None
        dict = {}
        for strr in strs:
            strrs = ''.join(sorted(strr))
            if strrs in dict.keys():
                dict[strrs].append(strr)
            else:
                dict[strrs] = [strr]
        return list(dict.values())
