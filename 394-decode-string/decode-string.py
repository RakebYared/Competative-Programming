class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for value in s:
            letters = deque()

            if value == ']':
                while stack[-1] != '[':
                    letters.appendleft(stack.pop())
                stack.pop()

                count = deque()
                while stack and len(stack[-1]) == 1 and ord(stack[-1]) >= ord('0') and ord(stack[-1]) <= ord('9'):
                    count.appendleft(stack.pop())
                
                count = int(''.join(count))

                stack.append(''.join(letters) * count)
            else:
                stack.append(value)
            
        return ''.join(stack)


    
        