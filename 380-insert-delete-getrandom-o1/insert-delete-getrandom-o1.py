class RandomizedSet:

    def __init__(self):
        self.my_list = []
        self.tracker = {}
        
    def insert(self, val: int) -> bool:
        if self.tracker.get(val, len(self.my_list)) < len(self.my_list):
            return False
        else:
            self.my_list.append(val)
            self.tracker[val] = len(self.my_list)-1
            return True

    def remove(self, val: int) -> bool:
        if self.tracker.get(val, len(self.my_list)) < len(self.my_list):
            self.my_list[self.tracker[val]] = self.my_list[-1]
            self.tracker[self.my_list[-1]] = self.tracker[val]
            self.my_list.pop()
            self.tracker.pop(val)
            return True
        else:
            return False
        
    def getRandom(self) -> int:        
        return random.choice(self.my_list)
    
      


# Your RandomizedSet object will be instantiated and called as such:
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()