class Solution:
    def flatten(self, head):
        if not head:
            return
        self.dfs(head)
        return head

    def dfs(self, head):
        if not head.child and not head.next:
            return head
        nxt = head.next
        child_last = None
        if head.child:
            child_last = self.dfs(head.child)
            head.next = head.child
            head.child.prev = head
            head.child = None
            if nxt:
                child_last.next = nxt
                nxt.prev = child_last
        if not nxt:
            return child_last
        else:
            return self.dfs(nxt)
