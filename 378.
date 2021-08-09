class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        pq = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(pq)
        for i in range(k - 1):
            num, x, y = heapq.heappop(pq)
            if y != n-1:
                heapq.heappush(pq, (matrix[x][y + 1], x, y + 1))
        return heapq.heappop(pq)[0]
 
