class Node:
    def __init__(self,val = None ,pre = None, nxt = None):
        self.val = val
        self.pre = pre
        self.next = nxt

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node()
        self.tail = Node()
        self.node = Node(homepage)

        self.head.next = self.node
        self.node.pre = self.head
        self.tail.pre = self.node
        self.node.next = self.tail

        

    def visit(self, url: str) -> None:
        new_node = Node(url)
        new_node.pre = self.node
        self.node.next = new_node
        self.tail = new_node.next
        self.node = new_node


    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.node.pre == self.head:
                break
            self.node = self.node.pre
        
        return self.node.val

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.node.next == self.tail:
                break
            self.node = self.node.next
        
        return self.node.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)