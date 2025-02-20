class Solution:
    def carPooling(self, trips: List[List[int]], cap: int) -> bool:
        max_distance = max(trips, key = lambda x: x[2])[2]
        print(max_distance)
        interval = [0]*(max_distance + 1)

        for num, start, end in trips:
            interval[start] += num
            interval[end] -= num
        
        for i in range(len(interval)):
            if interval[i] > cap:
                return False
            if i:
                interval[i] += interval[i-1]
                if interval[i] > cap:
                    return False
            
        return True
        # trips.sort(key = lambda x: x[1])

        # for i in range(len(trips)-1):
        #     num1, start1, end1 = trips[i]
        #     num2, start2, end2 = trips[i+1]

        #     if end1 > start2 and num1+num2 > cap:
        #         return False
        
        # return True
                