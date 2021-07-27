class LRUCache:
    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        self.head = DoubleLinkNode(-1, 0)
        self.tail = DoubleLinkNode(-2, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove_node(node)
            self.move2tail(node)
            return node.val
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove_node(node)
            self.move2tail(node)
        else:
            node = DoubleLinkNode(key, value)
            if self.size == self.capacity:
                self.remove_last_recent_node()
            self.add_node(node)
    
    def delete_key(self, key: int):
        self.cache.pop(key)
    
    def remove_last_recent_node(self):
        node = self.head.next
        self.delete_key(node.key)
        self.remove_node(node)
        self.size -= 1
    
    def remove_node(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def add_node(self, node):
        self.size += 1
        self.cache[node.key] = node
        self.move2tail(node)

    def move2tail(self, node):
        self.tail.prev.next, node.prev = node, self.tail.prev
        self.tail.prev, node.next = node, self.tail

class DoubleLinkNode:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None
