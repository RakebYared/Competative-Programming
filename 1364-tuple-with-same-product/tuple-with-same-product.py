class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        store = defaultdict(int)
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                store[nums[i]*nums[j]] += 1
            
        count = 0

        for val in store.values():
            if val > 1:
                count += (val*(val-1)//2) * 8
        
        return count 

        