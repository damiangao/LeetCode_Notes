class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        p = head
        for _ in range(k):
            if not p:
                return head
            p = p.next
        
        last = self.reverseK(head, k)
        head.next = self.reverseKGroup(head.next, k)
        return last
    
    def reverseK(self, head, k):
        pre, tmp = None, head
        for _ in range(k):
            nx = tmp.next
            tmp.next = pre
            pre = tmp
            tmp = nx
        head.next = nx
        return pre
