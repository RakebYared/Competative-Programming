# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap = []
        id = 0
        
        for head in lists:
            if head:
                heappush(heap, [head.val, id, head])
                id += 1

        dummy = ListNode()
        head = dummy
        

        while heap:
            node = heappop(heap)[-1]
          
            new_node = ListNode(node.val)
            head.next = new_node
            head = head.next

            if node.next:
                heappush(heap, [node.next.val, id, node.next])
                id += 1

        return dummy.next

