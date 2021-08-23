# elegant solution 
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        a %= 1337 
        if not b:
            return 1
        last = b.pop()
        part1 = self.mypow(a, last)
        part2 = self.mypow(self.superPow(a, b), 10)
        return part1 * part2 % 1337
    
    def mypow(self, a, k, base=1337):
        if k == 0:
            return 1
        if k % 2 == 1:
            return (a * self.mypow(a, k-1)) % base
        if k % 2 == 0:
            return (self.mypow(a, k // 2)) ** 2 % base

# naive solution
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if not b:
            return 1
        return a ** b[-1] * (self.superPow(a, b[:-1]) ** 10) % 1337
