class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for x in encoded:
            arr.append(x ^ arr[-1])
        return arr
