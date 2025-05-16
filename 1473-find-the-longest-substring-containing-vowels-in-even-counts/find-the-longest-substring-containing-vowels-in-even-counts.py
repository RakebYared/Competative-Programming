class Solution:
    def findTheLongestSubstring(self, s: str) -> int:

        index = {letter:i for letter, i in zip('aeiou', [0,1,2,3,4])}

        store = defaultdict(int)
        store[0] = -1

        state = 0
        ans = 0


        for i,letter in enumerate(s):

            if letter in index: 
                state ^= (1 << index[letter])
            
            if state in store:
                ans = max(ans, i - store[state])
            else:
                store[state] = i
              
            

        return ans
            