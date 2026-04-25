# naive solution
class Solution:
    _map = {
        "2":['a', 'b', 'c'],
        "3":['d', 'e', 'f'],
        "4":['g', 'h', 'i'],
        "5":['j', 'k', 'l'],
        "6":['m', 'n', 'o'],
        "7":['p', 'q', 'r', 's'],
        "8":['t', 'u', 'v'],
        "9":['w', 'x', 'y', 'z']
    }
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        return self.dfs(digits)

    def dfs(self, digits):
        if not digits:
            return [""]
        currents = self._map[digits[0]]
        succeeds = self.dfs(digits[1:])        
        return [x + y for x in currents for y in succeeds]
