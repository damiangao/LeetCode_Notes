class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        # max_num = arr[-1]
        # lost = max_num - len(arr)
        lost = []
        i = 1
        j = 0
        while i <= len(arr) + k:
            if j >= len(arr):
                lost.append(i)
            elif i!= arr[j]:
                while i < arr[j]:
                    lost.append(i)
                    i = i + 1
            i = i + 1
            j = j + 1

        return lost[k-1] 
