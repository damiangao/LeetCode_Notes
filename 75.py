class Solution:
    def swap(self, a, b, nums):
        nums[a], nums[b] = nums[b], nums[a]

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = curr = 0 # 左指针保证 l - 1以及之前的都是0
        r = len(nums)-1 # 右指针保证 r + 1以及之后的都是1
        while curr <= r:
            if nums[curr] == 0 :
                self.swap(l, curr, nums)
                l += 1
                curr += 1
            elif nums[curr] == 2:
                self.swap(r, curr, nums)
                r -= 1
            else:
                curr += 1
            




