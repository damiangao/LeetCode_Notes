#elegant solution
# dp table
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G = [0] * (n+1)
        G[0] = 1
        G[1] = 1
        for N in range(2, n+1):
            for i in range(1, N+1):
                G[N] += G[i-1] * G[N-i]

        return G[n]
