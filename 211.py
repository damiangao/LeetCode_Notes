class WordDictionary:
    def __init__(self):
        self.vocab = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.vocab
        for c in word:
            i = ord(c) - ord('a')
            if not cur.children[i]:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.vocab
        return self.searchFromMid(cur, word)

    def searchFromMid(self, cur, word):
        for idx, c in enumerate(word):
            if c == '.':
                for child in cur.children:
                    if child and self.searchFromMid(child, word[idx + 1:]):
                        return True
                return False
            i = ord(c) - ord('a')
            if not cur.children[i]:
                return False
            cur = cur.children[i]
        if cur.isEnd:
            return True
        return False

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
