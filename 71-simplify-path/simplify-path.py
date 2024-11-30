'''
iterate 
stack
join by / 
add / at the start

what not to append on to my stack
    1, ""
    2, .. and also pop here
    3, .
'''
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []
        for a in path:
            if stack and a == "..":
                stack.pop() 
                continue
            if not a or a=="." or a == "..":
                continue
            stack.append(a)
        return "/" + '/'.join(stack)

