class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:

        q = deque()
        n = len(nums)

        for i in range(k):
            while q and (q[-1][0] >= nums[i] or abs(q[-1][0] - nums[i]) > 1):
                q.pop()
            q.append([nums[i], i])
        
        ans = []
        ans.append(-1 if len(q) != k else q[-1][0])

        for i in range(n-k):
            if q[0] == [nums[i], i]:
                q.popleft()
            
            while q and ((q[-1][0] >= nums[i+k]) or abs(q[-1][0] - nums[i+k]) > 1 ):
                q.pop()
            q.append([nums[i+k], i+k])
        
       
            ans.append(-1 if len(q) != k else q[-1][0])
        return ans


    
        
