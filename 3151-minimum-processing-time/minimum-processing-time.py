class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse = True)
        n = len(tasks)
        max_time = 0
        j = 0

        for i in range(0,n,4):
            max_time = max(max_time, processorTime[j]+tasks[i])
            j += 1
        
        return max_time
