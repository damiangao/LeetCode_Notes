# elegant solution
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return 
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        backtrack(nums, [])
        return res
        
# mine
class Solution:
    def permute(self, nums):
        ret = []
        self.dfs(nums, 0, ret)
        return ret
    
    def dfs(self, nums, l, ret):
        if l == len(nums)-1:
            ret.append(copy.copy(nums))
            return
        for i in range(l, len(nums)):
            nums[l], nums[i] = nums[i], nums[l]
            self.dfs(nums, l+1, ret)
            nums[l], nums[i] = nums[i], nums[l]
        
# usage solution
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))
