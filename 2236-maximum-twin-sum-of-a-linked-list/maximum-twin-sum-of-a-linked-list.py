# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        previous = ListNode()

        while slow:
            temp = slow.next
            slow.next = previous
            previous = slow 
            slow = temp
        
        max_sum = 0
        
        while previous:
            max_sum = max(max_sum, previous.val + head.val)
            head = head.next
            previous = previous.next

        return max_sum
        