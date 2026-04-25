# O(n)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        mid = n / 2
        l, r = 0, 0
        for i in range(int(mid)):
            res, l, r = self.ne(l, r, nums1, nums2)
        res1, _, _ = self.ne(l, r, nums1, nums2)
        if mid%1 == 0:
            return (res1 + res) / 2
        return res1
    
    def ne(self, l, r, nums1, nums2):
        m, n = len(nums1), len(nums2)
        if l == m:
            return nums2[r], l, r+1
        if r == n:
            return nums1[l], l+1, r

        return (nums1[l], l+1, r) if nums1[l] < nums2[r] else (nums2[r], l, r+1)
