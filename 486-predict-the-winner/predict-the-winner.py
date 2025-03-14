class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def play(l, r):
            if l == r:
                return nums[l]

            right = nums[r] - play(l,r-1)
            left = nums[l] - play(l+1, r)

            return max(right, left)
        
        return play(0,len(nums)-1) >= 0


        