class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.dummy = Node()


    def get(self, index: int) -> int:
        node = self.dummy
        for _ in range(index):
            if not node.next:
                return -1
            node = node.next
        if node.next:
            return node.next.val
        else:
            return -1
        

    def addAtHead(self, val: int) -> None:
        new_node = Node(val, None)
        new_node.next = self.dummy.next
        self.dummy.next = new_node
        

    def addAtTail(self, val: int) -> None:
        new_node = Node(val,None)
        node = self.dummy
        while node.next:
            node = node.next
        node.next = new_node
        

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = Node(val, None)
        node = self.dummy
        for _ in range(index):
            if not node.next:
                return -1
            node = node.next
        
        new_node.next = node.next
        node.next = new_node
        
        

    def deleteAtIndex(self, index: int) -> None:
        
        node = self.dummy
        for _ in range(index):
            node = node.next
        if node and node.next:
            node.next = node.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)