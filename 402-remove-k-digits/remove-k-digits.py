class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:

        stack = []

        for num in nums:

            while stack and k and num < stack[-1]:
                stack.pop()
                k -= 1

            stack.append(num)

        
        while stack and k:
            stack.pop()
            k -= 1
        
        i = 0

        while i < len(stack):
            if stack[i] != '0':
                break
            i += 1


        stack = stack[i:]

        return ''.join(stack) if stack else '0'
        