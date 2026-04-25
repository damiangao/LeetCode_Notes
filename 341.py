class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = collections.deque(nestedList)

    def next(self) -> int:
        return self.nestedList.popleft()
    
    def hasNext(self) -> bool:
        while self.nestedList and not self.nestedList[0].isInteger():
            first = self.nestedList.popleft().getList()
            self.nestedList.extendleft(reversed(first))
        return bool(self.nestedList)
