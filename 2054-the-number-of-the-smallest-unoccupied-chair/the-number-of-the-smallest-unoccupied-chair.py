class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:

        store = {}
        
        order = []
        n = len(times)

        for i, time in enumerate(times):
            arr, leave = time
            order.append([arr, 1, i ])
            order.append([leave, -1, i ])
        
        order.sort()
        chair = [t for t in range(n)]

        for event in order:
            person = event[-1]

            if person in store:
                heappush(chair, store[person])
            
            else:
                store[person] = heappop(chair)
                if person == targetFriend:
                    return store[person]


 
