class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        p1, p2 = head, head
        while p1 and p1.next and p1.next.next:
            p1 = p1.next.next
            p2 = p2.next
            if p1 == p2:
                p3 = head
                while p3 != p2:
                    p2 = p2.next
                    p3 = p3.next
                return p2 
        return None
