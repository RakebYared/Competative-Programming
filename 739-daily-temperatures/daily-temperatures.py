class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        stack=[]
        ans = [0]*len(t)
        for i in range(len(t)):
            while stack and t[stack[-1]]<t[i]:
                ans[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        
        return ans