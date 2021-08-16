# Eratosthenes
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        isPrime = [1] * n
        isPrime[0] = 0
        isPrime[1] = 0
        i = 2
        while i * i < n:
            if isPrime[i]:
                j = i
                while j * i < n:
                    isPrime[j * i] = 0
                    j += 1
            i += 1
        return sum(isPrime) 
