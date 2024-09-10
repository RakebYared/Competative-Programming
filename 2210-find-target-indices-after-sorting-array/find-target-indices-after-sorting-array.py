class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res = [0]
        count = 0
        for a in nums:
            if a<target:
                res[0] += 1
            if a==target:
                count+=1
        for _ in range(1,count):
            res.append(res[-1]+1)
        return res if count!=0 else []


                




        
        