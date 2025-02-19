class Solution:
    def maxScore(self, s: str) -> int:
        store = {'1':0, '0':0}
        n = len(s)
        ones = s.count('1')
        max_score = 0

        for i in range(1,n):
            store[s[i-1]] += 1
            score = ones - store['1'] + store['0']
            max_score = max(max_score, score)
        
        return max_score


        