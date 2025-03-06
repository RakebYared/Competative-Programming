class DataStream:

    def __init__(self, value: int, k: int):
        self.arr_len = 0
        self.value = value 
        self.k = k
        

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.arr_len += 1
        else:
            self.arr_len = 0
        
        return True if self.arr_len >= self.k else False
        

        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)