class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        N, M = len(mat), len(mat[0])
        i, j = 0, 0
        direction = 1
        result = []
        
        while i < N and j < M:
            result.append(mat[i][j])
            
            new_i = i + (-1 if direction == 1 else 1)
            new_j = j + (1 if direction == 1 else -1)
            
            if new_i < 0 or new_i == N or new_j < 0 or new_j == M:
                if direction:
                    i += (j == M - 1)
                    j += (j < M - 1)
                else:
                    j += (i == N - 1)
                    i += (i < N - 1)    
                    
                direction = 1 - direction        
            else:
                i = new_i
                j = new_j                       
        return result  
