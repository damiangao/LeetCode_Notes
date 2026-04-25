class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = pre = ListNode()
        carry = 0
        while l1 or l2 or carry:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            cur_val = val % 10
            carry = val // 10
            pre.next = ListNode(cur_val)
            pre = pre.next
        return dummy.next
