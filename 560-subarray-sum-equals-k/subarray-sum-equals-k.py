class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ps = 0

        store = defaultdict(int)
        store[0] = 1
        count = 0

        for num in nums:
            ps += num
            count += store[ps - k]
            store[ps] += 1
        
        return count




        