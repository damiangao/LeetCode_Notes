# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(next=head)
        pre = dummy

        for _ in range(left - 1):
            pre = pre.next
        
        curr = pre.next

        for _ in range(right - left):
            nx = curr.next
            curr.next = nx.next
            nx.next = pre.next
            pre.next = nx
        return dummy.next
            
