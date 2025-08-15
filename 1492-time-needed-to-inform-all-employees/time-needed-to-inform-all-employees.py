class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        total_time = 0

        heap = [[0, headID]] # starting time of informing, id
        graph = [[] for _ in range(n)]

        for e in range(n):
            if manager[e] != -1: 
                graph[manager[e]].append(e)

        while heap:
            cur_time, node = heappop(heap)
            total_time = max(total_time, cur_time)

            for nei in graph[node]:
                heappush(heap, [cur_time + informTime[node], nei])
        # print(graph)
        return total_time


        


        