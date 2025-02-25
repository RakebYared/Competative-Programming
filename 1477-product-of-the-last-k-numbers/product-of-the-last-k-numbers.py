class ProductOfNumbers:

    def __init__(self):
        self.n = 1
        self.prefix = [1]
        

    def add(self, num: int) -> None:
        if num:
            self.prefix.append(num * self.prefix[-1])
            self.n += 1
        else:
            self.prefix = [1]
            self.n = 1

    def getProduct(self, k: int) -> int:
        if self.n <= k:
            return 0
        return self.prefix[-1] // self.prefix[-k-1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)