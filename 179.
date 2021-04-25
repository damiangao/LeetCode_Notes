# elegant solution
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y): return int(y+x) - int(x+y)
        nums = sorted(map(str, nums), key=cmp_to_key(compare))
        return "0" if nums[0]=="0" else "".join(nums)
