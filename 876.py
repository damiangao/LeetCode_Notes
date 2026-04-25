# elegant solution
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        p1 = p2 = head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        return p1
