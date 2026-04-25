class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        powersOfTwo = [2**i for i in range(22)]
        cnts, ans = Counter(), 0
        for num in deliciousness:
            for target in powersOfTwo:
                ans += cnts[target - num]
            cnts[num] += 1
        return ans % (10 ** 9 + 7)
