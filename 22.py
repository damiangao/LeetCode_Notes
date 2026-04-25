class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        track = []
    
        def backtrack(left, right, track):
            if left == n and right == n:
                ret.append(''.join(track))
            if left < n:
                track.append('(')
                backtrack(left + 1, right, track)
                track.pop()
            if left > right:
                track.append(')')
                backtrack(left, right + 1, track)
                track.pop()
        backtrack(0, 0, track)
        return ret
