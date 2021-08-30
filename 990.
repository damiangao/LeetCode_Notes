# naive solution
class Solution:
    def __init__(self):
        self.uf = UnionFind(26)

    def equationsPossible(self, equations: List[str]) -> bool:
        for eq in equations:
            if eq[1] == '=':
                self.uf.union(eq[0], eq[3])
                
        for eq in equations:
            if eq[1] == '!':
                if self.uf.connected(eq[0], eq[3]):
                    return False
        return True

class UnionFind:
    def __init__(self, n):
        self.count = n
        self.parent = {}
        for x in string.ascii_lowercase:
            self.parent[x] = x
        
    def count(self):
        return self.count
    
    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x
    
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootQ == rootP:
            return 
        
        self.parent[rootQ] = rootP
        self.count -= 1
    
    def connected(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        return rootP == rootQ
