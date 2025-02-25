# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        first_head = None
        second_head = None 
        node = head

        while node:
            if node.val < x:
                if not first_head:
                    first_head = node
                    first = node
                else:
                    first.next = node
                    first = node

            else:
                if not second_head:
                    second_head = node
                    second = node
                else:
                    second.next = node
                    second = node
        

            temp = node.next
            node.next = None 
            node = temp

        if first_head:
            first.next = second_head
        return first_head or second_head


        