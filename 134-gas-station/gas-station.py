class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(cost)
        rem = [(x - y) for x,y in zip(gas,cost)]
        if sum(rem) < 0:
            return -1
        
        min_index = 0
        max_ = 0
        start_index = 0

        rem += rem[:len(rem)-1]

        for i in range(1, len(rem)):
            rem[i] += rem[i-1]
        print(rem)
        for i,num in enumerate(rem):
            if num < rem[min_index]:
                min_index = i

            if num - rem[min_index] > max_:
                start_index = min_index

        return (start_index + 1) % n