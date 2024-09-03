class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        store = defaultdict(int)
        store[0] = 0
        for i in range(1,len(nums)):
            count = 0
            for j in store:
                if nums[i] < nums[j]:
                    store[j]+=1
                elif nums[i] > nums[j]:
                    count += 1
            store[i] = count
        return store.values()

        