# naive solution
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        lengths = [len(x) for x in dictionary]
        curr_idx = [0] * len(dictionary)
        ret, max_len = 0, 0
        for i in range(len(s)):
            for j in range(len(dictionary)):
                if curr_idx[j] < lengths[j]:
                    if dictionary[j][curr_idx[j]] == s[i]:
                        curr_idx[j] += 1
        for i in range(len(dictionary)):
            if curr_idx[i] == lengths[i]:
                if curr_idx[i] > max_len:
                    max_len = curr_idx[i]
                    ret = i
                elif curr_idx[i] == max_len:
                    ret = i if dictionary[ret] > dictionary[i] else ret
        return dictionary[ret] if curr_idx[ret] > 0 else "" 
