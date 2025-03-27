class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        low, high = max(weights), sum(weights)

        def checker(cap):
            count_days = 1
            carried_weight = 0

            for weight in weights:

                if carried_weight + weight > cap:
                    count_days += 1
                    carried_weight = 0
                
                carried_weight += weight
            
            return count_days <= days
        

        while high >= low:
            mid = (high + low) // 2

            if checker(mid):
                high = mid - 1
            else:
                low = mid  + 1

        return low 
        