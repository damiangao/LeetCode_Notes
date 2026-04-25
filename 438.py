# elegant solution
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = collections.defaultdict(int)
        window = collections.defaultdict(int)
        for x in p:
            need[x] += 1
        chars = len(need)
        l, r = 0, 0
        valid = 0
        ans = []
        while r < len(s):
            new_c = s[r]
            r += 1
            if need[new_c]:
                window[new_c] += 1
                if window[new_c] == need[new_c]:
                    valid += 1
            
            while r - l > len(p):
                del_c = s[l]
                l += 1
                if need[del_c]:
                    if window[del_c] == need[del_c]:
                        valid -= 1
                    window[del_c] -= 1
                    
            if chars == valid:
                ans.append(l)
        return ans
