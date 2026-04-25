# elegant solution
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ret = 0
        while l != r:
            dis = r - l
            if height[l] > height[r]:
                h = height[r]
                r -= 1
            else:
                h = height[l]
                l += 1
            ret = max(ret, dis * h)
        return ret
