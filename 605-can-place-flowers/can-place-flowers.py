class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        zeros = [1]
        for f in flowerbed:
            if f:
                zeros.append(0)
            else:
                zeros[-1] += 1
        
        zeros[-1] += 1
        
        for z in zeros:
            n -= (z-1)//2
        
        return True if n <= 0 else False