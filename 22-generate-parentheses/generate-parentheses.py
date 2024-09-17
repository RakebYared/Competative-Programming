class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def backtrack(Op,Cl):
            if Op==Cl==n:
                res.append(''.join(stack))
                return
            if Op<n:
                stack.append("(")
                backtrack(Op+1,Cl)
                stack.pop()
            if Cl<Op:
                stack.append(")")
                backtrack(Op,Cl+1)
                stack.pop()
        backtrack(0,0)
        return res
        