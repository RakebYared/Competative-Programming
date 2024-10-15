class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ave = sum(nums[0:k])/k
        maxave = ave
        for i in range(len(nums)-k):
            ave -= nums[i]/k
            ave += nums[i+k]/k
            maxave = max(maxave, ave)
        return maxave

        