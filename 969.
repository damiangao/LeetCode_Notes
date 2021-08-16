class Solution:
    def recurrence(self, arr):
        if len(arr) == 1:
            return
        max_idx = 0
        for i, x in enumerate(arr):
            if x > arr[max_idx]:
                max_idx = i
        if max_idx == 0:
            self.ret.append(len(arr))
            self.recurrence(list(reversed(arr[1:])))
        elif max_idx == len(arr) - 1:
            self.recurrence(arr[:-1])
        else:
            self.ret.append(max_idx + 1)
            self.recurrence(list(reversed(arr[:max_idx + 1])) + arr[max_idx + 1:])

    def pancakeSort(self, arr: List[int]) -> List[int]:
        self.ret = []
        self.recurrence(arr)
        return self.ret
