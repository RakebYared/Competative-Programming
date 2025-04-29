class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.k = k
        nums.sort()
        n = len(nums)
        if n > k:
            self.nums = nums[n-k:]
        else:
            self.nums = nums
        

    def add(self, val: int) -> int:
        heappush(self.nums, val)
        if len(self.nums) > self.k:
            heappop(self.nums)
        return self.nums[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)