class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        ret = -float("inf")
        cur_diff = float("inf")

        for first in range(n - 2):
            f_target = target - nums[first]
            second, third = first + 1, n - 1
            while second < third:
                if second > first + 1 and nums[second] == nums[second - 1]:
                    second += 1
                else:
                    sum_ = nums[second] + nums[third]
                    diff = abs(sum_ - f_target)
                    ret = ret if cur_diff < diff else nums[first] + nums[second] + nums[third]
                    cur_diff = min(diff, cur_diff)
                    if sum_ < f_target:
                        second += 1
                    elif sum_ > f_target:
                        third -= 1
                    elif sum_ == f_target:
                        return ret
        return ret
