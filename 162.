class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            l_val = nums[mid-1] if mid-1 >= 0 else -float('inf')
            r_val = nums[mid+1] if mid+1 < len(nums) else -float('inf')
            if nums[mid] > l_val and nums[mid] > r_val:
                return mid
            elif nums[mid] <= l_val:
                r = mid - 1
            else:
                l = mid + 1
    
