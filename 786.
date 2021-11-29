# elegant solution
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        left, right = 0.0, 1.0

        while True:
            mid = (left + right) / 2
            i, count = -1, 0
            x, y = 0, 1
            
            for j in range(1, n):
                while arr[i + 1] / arr[j] < mid:
                    i += 1
                    if arr[i] * y > arr[j] * x:
                        x, y = arr[i], arr[j]
                count += i + 1

            if count == k:
                return [x, y]
            
            if count < k:
                left = mid
            else:
                right = mid

# heap O(klogn) O(n)
class Frac:
    def __init__(self, idx: int, idy: int, x: int, y: int) -> None:
        self.idx = idx
        self.idy = idy
        self.x = x
        self.y = y
    
    def __lt__(self, other: "Frac") -> bool:
        return self.x * other.y < self.y * other.x
    
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        q = [Frac(0, i, arr[0], arr[i]) for i in range(n)] #[arr[0]/arr[0], [arr[0]]/arr[1],...arr[0]/arr[n-1]]
        heapq.heapify(q)
        for _ in range(k-1):
            frac = heapq.heappop(q)
            i, j = frac.idx, frac.idy
            heapq.heappush(q, Frac(i + 1, j, arr[i + 1], arr[j]))
        return [q[0].x, q[0].y]
