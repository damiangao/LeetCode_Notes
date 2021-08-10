class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        left, right = 0, n - 1
        left_max = right_max = 0
        ret = 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            
            if height[left] < height[right]:
                ret += left_max - height[left]
                left += 1
            else:
                ret += right_max - height[right]
                right -= 1
        return ret
