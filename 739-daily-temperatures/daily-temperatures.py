class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(t)
    
        for i in range(len(t)):
            while stack and t[i] > t[stack[-1]]:
                index = stack.pop()
                answer[index] = i - index
            stack.append(i)
    
        return answer