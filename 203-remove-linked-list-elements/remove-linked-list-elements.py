# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], num: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        node = dummy

        while node and node.next:
            if node.next.val == num:
                node.next = node.next.next
                continue 
            node = node.next
        return dummy.next