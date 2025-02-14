class Solution:
    def minimumSteps(self, s: str) -> int:
        
        swaps = 0
        holder = 0

        for seeker in range(len(s)):
            if s[seeker] == '0':
                swaps += (seeker - holder)
                holder += 1
        
        return swaps

        