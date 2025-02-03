class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        '''
        poping while len(stack)>=k:
        if stack[-k:] = stack[-1]*k
        stack = stack[:len(stack)-k]
        return stack

        12345
        '''
        stack = []
        for l in s:
            stack.append(l)
            while len(stack) >= k:
                if stack[-k:] == [stack[-1]]*k:
                    stack = stack[:len(stack)-k]
                else:
                    break
        return ''.join(stack)
           