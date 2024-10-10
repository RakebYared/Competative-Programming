class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for a in operations:
            if a == "+":
                stack.append(stack[-1]+stack[-2])
            elif a=="D":
                stack.append(2*stack[-1])
            elif a == "C":
                stack.pop()
            else:
                stack.append(int(a))
        return sum(stack)