class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None

        dummy = ListNode(next=head)
        pre = dummy
        cur = head
        while cur and cur.next:
            if cur.val != cur.next.val:
                cur = cur.next
                pre = pre.next
            else:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                cur = cur.next
                pre.next = cur
        return dummy.next
