class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt = {}
        for string in strs:
            ns = ''.join(sorted(string))
            if ns not in dictt:
                dictt[ns] = [string]
            else:
                dictt[ns].append(string)
        return list(dictt.values())


