class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        rows, cols = len(matrix), len(matrix[0])
        ret = []
        left, right, top, bottom = 0, cols - 1, 0, rows - 1
        while left <= right and top <= bottom:
            for col in range(left, right + 1):
                ret.append(matrix[top][col])
            for row in range(top + 1, bottom + 1):
                ret.append(matrix[row][right])
            if left < right and top < bottom:
                for col in range(right - 1, left, -1):
                    ret.append(matrix[bottom][col])
                for row in range(bottom, top, -1):
                    ret.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return ret

#  not elegant
class Solution(object):
    def __init__(self):
        self.ret = []
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        height = len(matrix)-1
        width = len(matrix[0])-1
        l, r, b, t = 0, width, 0, height

        while l < r and b < t:
            self.cycle(b, t, l, r, matrix)
            l += 1
            r -= 1
            b += 1
            t -= 1
        if l==r:
            for i in range(b, t+1):
                self.ret.append(matrix[i][l])
        elif b==t:
            for i in range(l, r+1):
                self.ret.append(matrix[b][i])
        return self.ret
    
    def cycle(self, h1, h2, w1, w2, matrix):
        i = w1
        while i <= w2:
            self.ret.append(matrix[h1][i])
            i += 1
        i = h1 + 1
        while i <= h2:
            self.ret.append(matrix[i][w2])
            i += 1
        i = w2 - 1
        while i >= w1:
            self.ret.append(matrix[h2][i])
            i -= 1
        i = h2 - 1
        while i >= h1 + 1:
            self.ret.append(matrix[i][w1])
            i -= 1
