class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # from i -> j-1 element xor ==
        # from j-> k element xor values 
        
        store = defaultdict(list)
        store[0] = [-1]

        ans = 0

        ps = 0

        for i,num in enumerate(arr):
            ps ^= num

            for index in store[ps]:
                ans += (i - index - 1)

            store[ps].append(i)
        
        return ans


