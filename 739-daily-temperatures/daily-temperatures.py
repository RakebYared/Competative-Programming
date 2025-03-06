class Solution:
    def dailyTemperatures(self, temperature: List[int]) -> List[int]:
        store = defaultdict(int)
        stack = []
        n = len(temperature)

        for i in range(n):
            while stack and temperature[stack[-1]] < temperature[i]:
                store[stack.pop()] = i - stack[-1]
            stack.append(i)
        
        ans = [store[i] for i in range(n)]
        return ans

        