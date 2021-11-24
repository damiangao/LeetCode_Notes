class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret = ""
        for cs in zip(*strs):
            if len(set(cs)) != 1:
                break
            ret += cs[0]
        return ret
