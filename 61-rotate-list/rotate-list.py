'''
find where the link breaks, which is after len-k jump
after that, if next is not none, make the next the new head
and in new loop, loop until none is found, and then connect that to the old head 
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        node = head 
        n = 1
        
        while node and node.next:
            n += 1
            node = node.next

        move = k % n

        node = head 
        for _ in range(n - move - 1):
            node = node.next

        new_head = head

        if node and node.next:
            new_head = node.next
            node.next = None
        
            node = new_head 
            while node.next:
                node = node.next
            
            node.next = head

        return new_head 