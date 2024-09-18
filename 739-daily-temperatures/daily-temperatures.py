class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        stack=[]

        for i in range(len(t)):
            if not stack:
                stack.append(i)
            else:
                while stack and t[stack[-1]]<t[i]:
                    t[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
        for a in stack:
            t[a]=0
        
        return t



