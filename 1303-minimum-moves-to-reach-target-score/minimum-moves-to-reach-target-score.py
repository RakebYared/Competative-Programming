class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = target - 1
        doubles = 0

        for _ in range(maxDoubles):
            if target < 3:
                break
            target //= 2
            ans -= target
            doubles += 1
        
        return ans + doubles
