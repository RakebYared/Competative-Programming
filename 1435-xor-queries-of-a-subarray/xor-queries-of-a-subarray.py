class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:

        arr = [0] + arr

        for i in range(1, len(arr)):
            arr[i] ^= arr[i-1]

        ans = []
        
        for l,r in queries:
            ans.append(arr[r+1] ^ arr[l])
        
        return ans

        