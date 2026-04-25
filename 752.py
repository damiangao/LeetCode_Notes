class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        visited = set()
        q = collections.deque(["0000"])
        visited.add("0000")
        step = 0
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur in deadends:
                    continue
                if cur == target:
                    return step
                for i in range(4):
                    up = self.plusOne(cur, i)
                    if not up in visited:
                        q.append(up)
                        visited.add(up)
                    down = self.minusOne(cur, i)
                    if not down in visited:
                        q.append(down)
                        visited.add(down)
            step += 1
        return -1
    def plusOne(self, s, i):
        s = list(s)
        t = int(s[i])
        if t == 9:
            t = '0'
        else:
            t = str(t+1)
        s[i] = t
        return "".join(s)

    def minusOne(self, s, i):
        s = list(s)
        t = int(s[i])
        if t == 0:
            t = '9'
        else:
            t = str(t-1)
        s[i] = t
        return "".join(s)
