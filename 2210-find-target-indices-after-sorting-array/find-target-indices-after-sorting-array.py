class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res = [0,0]
        for a in nums:
            if a<target:
                res[0] += 1
            if a==target:
                res[1] += 1

        return list(range(res[0], res[1]+res[0])) if res[1] !=0 else [] 


                




        
        