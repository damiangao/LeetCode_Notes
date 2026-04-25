class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.word = ""

    def insert(self, word):
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.is_word = True
        cur.word = word
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        def backtrack(now, i, j):
            if board[i][j] not in now.children:
                return 
            
            ch = board[i][j]
            nxt = now.children[ch]
            if nxt.word != "":
                ans.append(nxt.word)
                nxt.word = ""
            
            if nxt.children:
                board[i][j] = '#'
                for x, y in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
                    if 0 <= x <m and 0 <= y < n:
                        backtrack(nxt, x, y)
                board[i][j] = ch

            if not nxt.children:
                now.children.pop(ch)

        ans = []
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                backtrack(trie, i, j)
        return ans
