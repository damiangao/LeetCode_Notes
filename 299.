class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        cnt_s = collections.defaultdict(int, collections.Counter(secret))
        cnt_g = collections.defaultdict(int, collections.Counter(guess))
        check = collections.defaultdict(int)
        for x, y in zip(secret, guess):
            if x == y:
                check[x] += 1
                bulls += 1
        for num, times in cnt_g.items():
            cows += min(cnt_g[num], cnt_s[num]) - check[num]
        return str(bulls) + 'A' + str(cows) + 'B'
