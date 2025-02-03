class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        total_range = set()

        for start, end in ranges:
            for num in range(start, end+1):
                total_range.add(num) 
        for num in range(left,right+1):
            if num not in total_range:
                return False
        return True

            
