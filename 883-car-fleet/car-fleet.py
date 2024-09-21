class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position,speed)]
        stack = []
        for a in sorted(pair)[::-1]:
            if stack and (target-a[0])/a[1]<= stack[-1] :
                continue   
            stack.append((target-a[0])/a[1])
        
        return len(stack)