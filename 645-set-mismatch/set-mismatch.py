class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        ans = []

        store = set([x for x in range(1, len(nums)+1)])

        for num in nums:
            if num in store:
                store.remove(num)
            else:
                ans.append(num)


        return ans + list(store)
        