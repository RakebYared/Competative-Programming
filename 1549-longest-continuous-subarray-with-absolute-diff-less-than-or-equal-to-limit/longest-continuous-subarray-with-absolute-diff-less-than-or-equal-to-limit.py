class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ans = 0
        max_q = deque()
        min_q = deque()
        n = len(nums)

        l = 0
        for r in range(n):
            while max_q and max_q[-1] < nums[r]:
                max_q.pop()
            while min_q and min_q[-1] > nums[r]:
                min_q.pop()
            
            max_q.append(nums[r])
            min_q.append(nums[r])

            if max_q[0] - min_q[0] > limit:
                while True:
                    if  nums[l] == max_q[0]:
                        max_q.popleft()
                        break 
                    if  nums[l] == min_q[0]:
                        min_q.popleft()
                        break 
                    l += 1 
                l += 1

            ans = max(ans, r-l+1)
        return ans