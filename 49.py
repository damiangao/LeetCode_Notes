class Solution:
    def __init__(self):
        self.map = collections.defaultdict(list)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        for s in strs:
            s_sort = sorted(s)
            self.map["".join(s_sort)].append(s)
        return list(self.map.values())
