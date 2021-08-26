# elegant solution O(log(n)) O(n)
class ExamRoom(object):
    # pair两头开
    def __init__(self, N):
        self.n = N
        self.pair_l2r = {}
        self.pair_r2l = {}
        self.heap = []
        self.push_pair(-1, self.n)

    def seat(self):
        l, r = self.longest_pair()
        if l == r - 1:
            ret = -1
        if l == -1:
            ret = 0
        elif r == self.n:
            ret = r - 1
        else:
            ret = l + ((r - l) >> 1)
        self.pair_l2r.pop(l, -2)
        self.pair_r2l.pop(r, -2)

        self.push_pair(l, ret)
        self.push_pair(ret, r)
        return ret

    def leave(self, p):
        l = self.pair_r2l.pop(p, p - 1)
        r = self.pair_l2r.pop(p, p + 1)
        self.pair_l2r.pop(l, -2)
        self.pair_r2l.pop(r, -2) 
        self.push_pair(l, r)

    def push_pair(self, l, r):
        if -1 <= l < r <= self.n and l < r - 1:
            if l == -1 or r == self.n:
                dist = r - l - 1
            else:
                dist = (r - l) // 2
            heapq.heappush(self.heap, (-dist, l, r))
            self.pair_l2r[l] = r
            self.pair_r2l[r] = l

    def longest_pair(self):
        l = r = -2
        while self.heap:
            _, l, r = heapq.heappop(self.heap)
            if self.pair_l2r.get(l, -99) == r and self.pair_r2l.get(r, -99) == l:
                break
        return l, r
        
# naive solution O(n)
class ExamRoom(object):
    def __init__(self, N):
        self.n = N
        self.students = [] # 学生座位情况，当前落座位置的有序列表

    def seat(self):

        if not self.students:
            # 位置全空, 下个位置为0
            next_seat = 0
        else:
            dist, next_seat = self.students[0], 0
            for i, pos in enumerate(self.students):
                if i:
                    # 遍历每个间隔
                    prev = self.students[i - 1]
                    d = (pos - prev) // 2
                    if d > dist:
                        dist, next_seat = d, prev + d
            # 考虑最后一个学生到最后一个座位的间隔
            d = self.n - 1 - self.students[-1]
            if d > dist:
                next_seat = self.n - 1
        bisect.insort(self.students, next_seat)
        return next_seat

    def leave(self, p):
        self.students.remove(p)
