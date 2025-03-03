# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pre1 = None 
        pre2 = None

        while l1:
            temp = l1.next
            l1.next = pre1
            pre1 = l1
            l1 = temp

        
        while l2:
            temp = l2.next
            l2.next = pre2
            pre2 = l2
            l2 = temp
        
        carry = 0
        ans = None

        while pre1 or pre2:
            if pre1:
                carry += pre1.val
                pre1 = pre1.next
            
            if pre2:
                carry += pre2.val
                pre2 = pre2.next

            node = ListNode(carry%10, ans)
            ans = node

            carry //= 10
        
        if carry:
            node = ListNode( 1, ans)
            ans = node
        
        return ans
            





            