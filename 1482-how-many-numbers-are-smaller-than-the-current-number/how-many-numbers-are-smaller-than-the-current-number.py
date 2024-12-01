class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        order = [0]*101
        for num in nums:
            order[num]+=1
        for i in range(1,len(order)):
            order[i]+= order[i-1]
        for num in nums:
            res.append(order[num-1] if num!=0 else 0)

        return res
