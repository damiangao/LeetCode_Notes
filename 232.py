class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l = []
        self.r = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.l.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        ret = self.peek()
        self.r.pop()
        return ret

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.r:
            return self.r[-1]
        
        if not self.l:
            return None
        
        while self.l:
            self.r.append(self.l.pop())
        return self.r[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.l and not self.r
