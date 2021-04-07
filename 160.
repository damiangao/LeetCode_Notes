# solution1
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len1, len2 = 0, 0
        tempA, tempB = headA, headB
        while tempA:
            tempA = tempA.next
            len1 += 1
        
        while tempB:
            tempB = tempB.next
            len2 += 1
        
        dis = len1 - len2
        if dis > 0:
            for _ in range(dis):
                headA = headA.next
        else:
            for _ in range(-dis):
                headB = headB.next
        
        while headA and headB and headA != headB:
            headA = headA.next
            headB = headB.next
        
        return headA

# solution 2
class Solution(object):
  def getIntersectionNode(self, headA, headB):
      """
      :type head1, head1: ListNode
      :rtype: ListNode
      """
      if headA == headB:
          return headA
      p1, p2 = headA, headB
      while p1 and p2:
          p1 = p1.next
          p2 = p2.next

      if not p1:
          p1 = headB
      if not p2:
          p2 = headA

      while p1 and p2:
          p1 = p1.next
          p2 = p2.next

      if not p1:
          p1 = headB
      if not p2:
          p2 = headA

      while p1 and p2:
          if p1 == p2:
              return p1
          p1 = p1.next
          p2 = p2.next

      return None
