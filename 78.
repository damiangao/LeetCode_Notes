class Solution:
    def __init__(self):
        self.res = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        track = [] # 用来记录当前的路径
        self.backtrack(nums, 0, track)
        return self.res
    
    def backtrack(self, nums, start, track):
        self.res.append(track[::])
        for i in range(start, len(nums)):
            track.append(nums[i])
            self.backtrack(nums, i + 1, track)
            track.pop()
