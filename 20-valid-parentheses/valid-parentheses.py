class Solution:
    def isValid(self, s: str) -> bool:
        store= {")":"(", "}":"{", "]":"["}
        stack = []
        for a in s:
            if not stack and a in store :
                return False
            if stack and a in store :
                if store[a] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(a)
        return False if stack else True

