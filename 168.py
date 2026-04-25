#elegant solution
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            res.append(chr((columnNumber - 1) % 26 + ord('A')))
            columnNumber = (columnNumber - 1) // 26
        return "".join(reversed(res))
