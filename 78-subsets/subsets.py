class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def create(store, i):
            if i == n:
                ans.append(store.copy())
                return 

            store.append(nums[i])
            create(store, i + 1)
            store.pop()
            create(store, i + 1)

        create([],0)
        return ans

        


            
                

