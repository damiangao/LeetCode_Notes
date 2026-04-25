# elegant solution
class Solution:
    def __init__(self) -> None:
        self._dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def romanToInt(self, s: str) -> int:
        ret = i = 0
        while i < len(s):
            if i < len(s) - 1 and self._dict[s[i]] < self._dict[s[i+1]]:
                ret -= self._dict[s[i]]
            else:
                ret += self._dict[s[i]]
            i += 1
        return ret

# naive solution
class Solution:
    def __init__(self) -> None:
        self._dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

    def romanToInt(self, s: str) -> int:
        ret = i = 0
        while i < len(s):
            c1 = s[i]
            if i < len(s) - 1:
                c2 = s[i: i+2]
            else:
                c2 = ''

            if c2 and c2 in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
                ret += self._dict[c2]
                i += 2
                continue
            
            ret += self._dict[c1]
            i += 1
        return ret
