# elegant solution
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        p1 = p2 = head
        while p1 and p1.next:
            p1 = p1.next.next
            p2 = p2.next
            if p1 == p2:
                return True
        return False
