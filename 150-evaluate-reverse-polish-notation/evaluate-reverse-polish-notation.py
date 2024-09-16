class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        h = {"+":lambda x,y:x+y,
            "*":lambda x,y:x*y,
            "-":lambda x,y:x-y,
            "/":lambda x,y:int(x/y) }
        st = []
        for a in tokens:
            if a in h:
                c = h[a](st[-2],st[-1])
                st.pop()
                st.pop()
                st.append(c)
            else:
                st.append(int(a))
        return st[-1]
        