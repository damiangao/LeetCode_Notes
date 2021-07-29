class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        s = []
        for i in reversed(range(n * 2 - 1)):
            while s and nums[i % n] >= s[-1]:
                s.pop()
            
            ans.append(s[-1] if s else -1)
            s.append(nums[i % n])

        ans.reverse()
        return ans[:n]
