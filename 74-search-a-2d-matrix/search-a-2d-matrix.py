class Solution:
    def searchMatrix(self, m: List[List[int]], t: int) -> bool: 
        r, c = len(m), len(m[0])

        low, high = 0, r-1

        while high >= low:
            mid = (high + low) // 2

            if m[mid][0] == t:
                return True
            elif m[mid][0] > t:
                high = mid - 1
            else:
                low = mid + 1
        
        row = high

        low, high = 0, c-1

        while high >= low:
            mid = (high + low) // 2

            if m[row][mid] == t:
                return True
            elif m[row][mid] > t:
                high = mid - 1
            else:
                low = mid + 1
        
        return False
        


        