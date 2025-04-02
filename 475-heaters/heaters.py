class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()

        def checker(mid):
            j = 0
            for i in range(len(houses)):

                while j < len(heaters)-1 and heaters[j] < houses[i]:
                    j += 1
                
                dis = min(abs(houses[i] - heaters[j]), abs(houses[i] - heaters[j-1]))
                if dis > mid:
                    return False

            return True

        low, high = 0, max(heaters[-1], houses[-1]) - min(houses[0], heaters[0])
        print(checker(1))

        while high >= low:
            mid = (high + low) // 2

            if checker(mid):
                high = mid - 1
            else:
                low = mid + 1
        
        return low

        
       