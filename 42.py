class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [height[0]] * n
        right = [height[n-1]] * n
        ret = 0

        for i in range(1, n):
            left[i] = max(left[i-1], height[i])
        
        for j in reversed(range(0, n-1)):
            right[j] = max(right[j+1], height[j])

        for k in range(n):
            min_height = min(left[k], right[k])
            if min_height > height[k]:

                ret +=  (min_height - height[k])
        return ret


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1
        lh = height[0]
        rh = height[n-1]
        ret = 0

        while l < r:   
            min_h = min(lh, rh)
            if lh < rh:
                if min_h > height[l]:
                    ret +=  min_h - height[l]
                l += 1
                lh = max(lh, height[l])
            else:
                if min_h > height[r]:
                    ret +=  min_h - height[r]
                r -= 1
                rh = max(rh, height[r])
        return ret
