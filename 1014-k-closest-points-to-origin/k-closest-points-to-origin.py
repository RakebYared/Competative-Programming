class Solution:
    def swap(self,points, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
        points[i], points[j] = points[j], points[i]
 
    def sift(self,points, nums, i, upper):
        while True:
            l, r = (i * 2) + 1, (i * 2) + 2  
            small = i
            
            if l < upper and nums[l] < nums[small]:
                small = l
            if r < upper and nums[r] < nums[small]: 
                small = r
            
            if small != i: 
                self.swap(points, nums, i, small)
                i = small 
            else:
                break

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        nums = []
        for a in points:
            nums.append(math.sqrt(pow(a[0],2) + pow(a[1],2)))
       
        for i in range((len(nums) // 2) - 1, -1, -1):
            self.sift(points, nums, i, len(nums))
        
        for end in range(len(nums) - 1, len(nums)-1-k, -1):
            self.swap(points,nums, 0, end)
            self.sift(points,nums, 0, end)
        
        return points[len(points)-k:]