class Solution:
    def convert(self, s: str, numRows: int) -> str:
        numRows = min(numRows, len(s))
        if numRows == 1:
            return s
        ret = [[] for _ in range(numRows)]
        cur_row = 0
        godown = False
        for c in s:
            ret[cur_row].append(c)
            if cur_row == 0 or cur_row == numRows - 1:
                godown = not godown
            cur_row += 1 if godown else -1
        return "".join(["".join(x) for x in ret])
