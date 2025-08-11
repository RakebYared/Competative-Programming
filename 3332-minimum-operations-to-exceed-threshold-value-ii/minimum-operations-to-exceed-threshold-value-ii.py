class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        nums.sort()
        count = 0

        while len(nums) >= 2: 
            x,y = heappop(nums), heappop(nums)
            
            if x >= k and y >= k:
                break

            count += 1

            new_num = min(x, y) * 2 + max(x, y)
            heappush(nums, new_num)

        return count 

        