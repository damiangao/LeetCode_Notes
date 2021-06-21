class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for i in range(1024):
            h, m = i >> 6, i & 0x3f
            if h < 12 and m < 60 and bin(i).count('1') == turnedOn:
                res.append(f"{h}:{m:02d}")
        return res
