# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def findmid(head):
            slow, fast = head, head.next
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow

        def mergesort(head):
            if not head or (not head.next):
                return head

            mid = findmid(head)

            right = mergesort(mid.next)
            mid.next = None
            left = mergesort(head)

            node = ListNode()
            dummy = node

            while right and left:
                if left.val < right.val:
                    dummy.next = ListNode(left.val)
                    left = left.next
                else:
                    dummy.next = ListNode(right.val)
                    right = right.next

                dummy = dummy.next

            if right:
                dummy.next = right
            if left:
                dummy.next = left
            
            return node.next
                
        return mergesort(head)

            
        