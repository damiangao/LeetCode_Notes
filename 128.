class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ret = 0
        nums = set(nums)

        for num in nums:
            if num - 1 not in nums:
                curr_len = 1
                curr_num = num

                while curr_num + 1 in nums:
                    curr_num += 1
                    curr_len += 1
                ret = max(ret, curr_len)
        return ret
