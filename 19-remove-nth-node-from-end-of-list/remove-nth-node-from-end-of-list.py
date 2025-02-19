# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        node1, node2 = dummy, dummy
        for _ in range(n+1):
            node2 = node2.next
        
        while node2:
            node1 = node1.next
            node2 = node2.next
        
        node1.next = node1.next.next
        return dummy.next
        
     