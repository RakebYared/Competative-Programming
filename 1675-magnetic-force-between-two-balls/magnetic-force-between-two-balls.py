class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        n = len(position)
        position.sort()
        ans = 0

        low, high = 1, position[-1] - position[0]

        def checker(force):
            balls_placed = 2
            last_position = position[0]

            for curr_position in position[1:n-1]:
                if curr_position - last_position >= force:
                    balls_placed += 1
                    last_position = curr_position
                if balls_placed == m:
                    break
            
            
            return position[-1] - last_position >= force and balls_placed >= m
      
        
        while high >= low:
            mid = (high + low) // 2

            if checker(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans
        