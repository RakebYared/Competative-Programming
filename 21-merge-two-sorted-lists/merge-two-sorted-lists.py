# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = list1
        n1 = dummy
        n2 = list2

        while n1 and n1.next and n2:
            if n1.next.val < n2.val:
                n1 = n1.next

            else:
                temp = n2.next
                n2.next = n1.next
                n1.next = n2
                n2 = temp 
                n1 = n1.next
        while n1 and n1.next:
            n1 = n1.next
        n1.next = n2
           
        return dummy.next


        