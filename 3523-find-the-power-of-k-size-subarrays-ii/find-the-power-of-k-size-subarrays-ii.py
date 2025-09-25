class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:

        maxx = deque()
        minn = deque()
        n = len(nums)

        for i in range(k):
            while maxx and (nums[i] <= maxx[-1][0] or abs(nums[i] - maxx[-1][0]) > 1 ):
                maxx.pop()
            maxx.append([nums[i], i])

            while minn and (nums[i] >= minn[-1][0] or abs(nums[i] - minn[-1][0]) > 1 ):
                minn.pop()
            minn.append([nums[i], i])

        ans = []
        ans.append(maxx[-1][0] if len(maxx) == k else -1)

        for i in range(n - k):
            
            if minn[0] == [nums[i],i]:
                minn.popleft()
            if maxx[0] == [nums[i], i]:
                maxx.popleft()

            while maxx and (nums[i+k] <= maxx[-1][0] or abs(nums[i+k] - maxx[-1][0] ) > 1) :
                maxx.pop()
            maxx.append([nums[i+k], i+k])

            while minn and (nums[i+k] >= minn[-1][0] or abs(nums[i+k] - minn[-1][0]) > 1 ):
                minn.pop()
            minn.append([nums[i+k], i+k])


            ans.append(maxx[-1][0] if len(maxx) == k else -1)

        return ans
        