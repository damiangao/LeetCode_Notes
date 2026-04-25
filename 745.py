# hash
class WordFilter:

    def __init__(self, words: List[str]):
        self.d = {}
        for i, word in enumerate(words):
            m = len(word)
            for prefix_len in range(1, m + 1):
                for suff_len in range(1, m + 1):
                    self.d[word[:prefix_len]+'#'+word[-suff_len:]] = i
    def f(self, pref: str, suff: str) -> int:
        return self.d.get(pref+'#'+suff, -1)

# Trie
class TrieNode:
    def __init__(self):
        self.child = {}
        self.isWord = False 
        self.pos = -1
class WordFilter:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for pos,word in enumerate(words):    
            tmp = word + '#' + word             
            for i in range(len(word) + 1):
                rt = self.root
                for c in tmp[i: ]:              
                    if c not in rt.child:
                        rt.child[c] = TrieNode()
                    rt = rt.child[c]
                    rt.pos = pos
    def f(self, prefix: str, suffix: str) -> int:
        rt = self.root
        tmp = suffix + '#' + prefix
        for c in tmp:
            if c not in rt.child:
                return -1
            rt = rt.child[c]
        return rt.pos
