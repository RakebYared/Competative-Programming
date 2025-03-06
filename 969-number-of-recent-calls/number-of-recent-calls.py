'''
prepare deque 
every new request :
    im gonna check if all the items in q are valid meaning their difference from the new request is not > 3000
    return len(q)
'''
class RecentCounter:

    def __init__(self):
        self.queque = deque()        

    def ping(self, t: int) -> int:
        while self.queque and t - self.queque[0] > 3000:
            self.queque.popleft()
        self.queque.append(t)
        return len(self.queque)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)