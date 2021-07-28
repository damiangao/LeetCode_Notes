class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.KF = dict()
        self.FKs = dict()

    def get(self, key: int) -> int:
        if key in self.KF:
            val = self.FKs[self.KF[key]][key]
            self.update_freq(key)
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.KF:
            self.FKs[self.KF[key]][key] = value
            self.update_freq(key)
        else:
            if self.capacity == self.size:
                self.pop()
            self.add(key, value)

    def update_freq(self, key):
        node_freq = self.KF[key]
        val = self.FKs[node_freq][key]
        self.KF[key] += 1
        self.FKs[node_freq].pop(key)
        self.add_FKs(node_freq+1, key, val)

        if node_freq == self.min_freq and not self.FKs[self.min_freq]:
            self.min_freq += 1

    def pop(self):
        key, _ = self.FKs[self.min_freq].popitem(last=False)
        self.KF.pop(key)
        self.size -= 1

    def add(self, key, val):
        self.KF[key] = 1
        self.add_FKs(1, key, val)
        self.size += 1
        self.min_freq = 1
    
    def add_FKs(self, freq, key, value):
        if freq not in self.FKs:
            self.FKs[freq] = collections.OrderedDict()
        self.FKs[freq][key] = value
