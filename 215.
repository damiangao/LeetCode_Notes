# elegant solution
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = [-x for x in nums]
        heapq.heapify(nums)
        for _ in range(k):
            res = heapq.heappop(nums)
        return -res
        
# classic solution
class Solution:
    def __init__(self):
        self.nums = []
        self.len = 0
    def findKthLargest(self, nums, k):
        self.nums = nums
        self.len = len(self.nums)
        self.heap_build()
        while k:
            ret = self.pop()
            k -= 1
        return ret

    def heapify(self, i):
        l = i*2 + 1
        while l < self.len:
            r = l + 1
            max_i = i if max(self.nums[l], self.nums[i]) == self.nums[i] else l
            if r < self.len:
                max_i = max_i if max(self.nums[max_i], self.nums[r]) == self.nums[max_i] else r
            if i == max_i:
                break
            self.nums[i], self.nums[max_i] = self.nums[max_i], self.nums[i]
            i = max_i
            l = i * 2 + 1

    def heap_build(self):
        i = self.len // 2
        while i >= 0:
            self.heapify(i)
            i -= 1

    def pop(self):
        ret = self.nums[0]
        self.nums[0] = self.nums[self.len-1]
        self.len -= 1
        self.heapify(0)
        return ret
