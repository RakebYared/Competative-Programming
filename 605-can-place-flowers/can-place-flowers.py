class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flag = False
        count = 0

        for f in flowerbed:
            if f:
                if flag:
                    count -= 1
                flag = True

            elif flag:
                flag =  False

            else:
                count += 1
                flag = True
            
        return True if count >= n else False
