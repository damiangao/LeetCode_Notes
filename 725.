class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        length = 0
        temp = head
        ret = []
        while temp:
            temp = temp.next
            length += 1
        
        u, v = length // k, length % k
        sizes = []
        for i in range(k):
            if i < v:
                sizes.append(u + 1)
            else: 
                sizes.append(u)
        seq = [None] * k
        temp = head
        for i, l in enumerate(sizes):
            if not temp:
                break
            head = temp
            seq[i] = head
            for _ in range(l - 1):
                head = head.next
            temp = head.next
            head.next = None
        return seq
