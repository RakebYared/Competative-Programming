class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        op = {"++X":lambda x:x+1, "X++":lambda x:x+1, "--X":lambda x:x-1, "X--":lambda x:x-1}
        res = 0
        for a in operations:
            res = op[a](res)
        
        return res
        


        