#elegant solution
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = collections.defaultdict(int)
        for x in s1:
            need[x] += 1
        chars, l1 = len(need), len(s1)
        window = collections.defaultdict(int)
        l = r = 0
        valid = 0
        while r < len(s2):
            new_c = s2[r]
            r += 1      
            if need[new_c]:
                window[new_c] += 1
                if window[new_c] == need[new_c]:
                    valid += 1

            while r - l >= l1:
                if valid == chars:
                    return True
                del_c = s2[l]
                l += 1
                if need[del_c]:
                    if window[del_c] == need[del_c]:
                        valid -= 1
                window[del_c] -= 1
            
        return False
