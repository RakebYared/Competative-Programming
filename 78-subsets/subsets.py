class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def create(store, i):
            
            ans.append(store.copy())

            for i in range(i, n):
                store.append(nums[i])
                create(store, i + 1)
                store.pop()

        create([],0)
        return ans

        


            
                

