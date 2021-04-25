class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        d = defaultdict(ListNode)

        pre_sum = 0
        dummy = ListNode(0)
        dummy.next = head
        p = dummy

        while p:
            pre_sum += p.val
            d[pre_sum] = p
            p = p.next
        
        p = dummy
        pre_sum = 0
        while p:
            pre_sum +=p.val
            p.next = d[pre_sum].next
            p = p.next
        
        return dummy.next
