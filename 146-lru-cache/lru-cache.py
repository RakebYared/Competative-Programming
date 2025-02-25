class Node:
    def __init__(self, val = 0, pre = None ,nex = None):
        self.val = val  
        self.next = nex
        self.pre = pre

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity

        self.head = Node()
        self.tail = Node()
        
        self.head.next = self.tail
        self.tail.pre = self.head

        self.store = {}  # key to node pair
    
    def add(self, new_node):
        new_node.pre = self.tail.pre
        new_node.next = self.tail 
        self.tail.pre.next = new_node
        self.tail.pre = new_node
      
    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        
        new_node = Node(self.store[key].val)
        self.remove(self.store[key])
        self.add(new_node)
        self.store[key] = new_node

        return new_node.val[1]

        

    def put(self, key: int, value: int) -> None:

        if key in self.store:
            self.remove(self.store[key])
        
        elif self.cap == len(self.store):
            self.store.pop(self.head.next.val[0])
            self.remove(self.head.next)
        
        new_node = Node([key, value])
        self.add(new_node)
        self.store[key] = new_node



        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)