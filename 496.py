class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        N = len(nums2)
        search = {}
        ret = []
        s = []

        for i in reversed(range(N)):
            while s and nums2[i] > s[-1]:
                s.pop()
            search[nums2[i]] = s[-1] if s else -1
            s.append(nums2[i])
        
        for x in nums1:
            ret.append(search[x])
        return ret
