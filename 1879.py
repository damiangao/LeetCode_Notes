class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        f = [float("inf")] * (1 << n)
        f[0] = 0
        for mask in range(1, 1 << n):
            c = bin(mask).count("1")
            for i in range(n):
                if mask & (1 << i):
                    f[mask] = min(f[mask], f[mask ^ (1 << i)] + (nums1[c-1] ^ nums2[i]))
        return f[(1 << n) - 1]
