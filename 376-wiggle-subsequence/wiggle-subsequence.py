'''
to alternate the nums big small big ... or small big small
i will have to use different stacks for this 
im using stack to keep track of the valid subcequence 

if the stack[-1] is considered big (flag = True) my aim is to find a smaller number or else replace it with a bigger number

and vise versa 
'''
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        flag = False
        ans = 0
        
        for _ in range(2):
            stack = []
            for num in nums:
                if stack:
                    if flag and num >= stack[-1]:
                        stack.pop()
                
                    elif not flag and num <= stack[-1]: 
                        stack.pop()
                        
                    else:      
                        flag = not flag

                stack.append(num)
            ans = max(ans, len(stack))
            flag = True

        return ans