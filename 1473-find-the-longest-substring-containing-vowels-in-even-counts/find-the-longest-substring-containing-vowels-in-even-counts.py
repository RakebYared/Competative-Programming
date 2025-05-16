class Solution:
    def findTheLongestSubstring(self, s: str) -> int:

        bit = [0, 0, 0, 0, 0]
        index = {letter:i for letter, i in zip('aeiou', [0,1,2,3,4])}

        store = defaultdict(int)
        store[(0,0,0,0,0)] = -1

        ans = 0


        for i,letter in enumerate(s):

            if letter in index: 
                bit[index[letter]] += 1 
                bit[index[letter]] %= 2


            
            check = tuple(bit)



            if check not in store:
                store[check] = i
           

            else:
                ans = max(ans,  i - store[check])
            

        return ans
            