class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        heap = nums[:k]

        for num in nums[k:]:
            heappush(heap, num)
            heappop(heap)
        
        return heap[0]


        

        
        