# elegant solution
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.parents = list(range(len(edges)+1))
        for u, v in edges:
            up = self.find(u)
            vp = self.find(v)
            if up == vp:
                return [u, v]
            else:
                self.parents[up] = vp

    def find(self, i):
        while i != self.parents[i]:
            i = self.parents[i]
        return i
