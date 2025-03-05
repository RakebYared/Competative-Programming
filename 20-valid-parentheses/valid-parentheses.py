class Solution:
    def isValid(self, s: str) -> bool:
        store = {'(':')', '[':']', '{':'}'}
        stack = []

        for i in s:
            if i in store:
                stack.append(i)
            elif stack and store[stack[-1]] == i:
                stack.pop()
            else:
                return False

        return True if not stack else False