class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)

        tasks = [task + [i] for i,task in enumerate(tasks)]
        tasks.sort()

        # print(tasks)

        now = tasks[0][0]
        i = 0
        heap = []
        ans = []


        while True:

            while i < n and tasks[i][0] <= now:
                heappush(heap, tasks[i][1:])
                i += 1

            if heap:

                processing_time, index = heappop(heap)
                ans.append(index)

                now += processing_time

            else:
                if i < n:
                    now = tasks[i][0]
                else:
                    return ans


        
            