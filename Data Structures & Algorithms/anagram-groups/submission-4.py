class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return None
        dictt = {}
        for s in strs:
            ss = str(sorted(s))
            if ss in dictt:
                dictt[ss].append(s)
            else:
                dictt[ss] = [s]
        return list(dictt.values())
            