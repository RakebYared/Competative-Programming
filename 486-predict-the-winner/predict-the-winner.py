class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        dp = {}
        def play(l, r):
            if (l,r) in dp:
                return dp[(l,r)]

            if l == r:
                return nums[l]

            right = nums[r] - play(l,r-1)
            left = nums[l] - play(l+1, r)

            dp[(l,r)] = max(right, left) 

            return dp[(l,r)]
        
        return play(0,len(nums)-1) >= 0


        