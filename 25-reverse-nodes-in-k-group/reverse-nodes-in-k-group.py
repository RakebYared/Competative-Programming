# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        counter = head
        n = 0

        while counter:
            counter = counter.next
            n += 1

        node = head
        ans = head
        start = None

        while node:
            pre = None
            start, end = node, start

            if n < k:
                end.next = start
                return ans
            
            for _ in range(k):       
                temp = node.next
                node.next = pre
                pre = node
                node = temp     
            
            if end:
                end.next = pre
            else:
                ans = pre
            n -= k
        
        return ans


            


