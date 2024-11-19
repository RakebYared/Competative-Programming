class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        store = defaultdict(list)
        store[nums[0]].append(0)
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
            store[nums[i]].append(i)
        for i in range(len(nums)):
            for a in store[nums[i]-k]:
                if a>=i: break
                count+=1
            if nums[i] == k:
                count+=1
        return count
