class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        store = defaultdict(int)
        for a  in text:
            store[a]+=1
        return min(store['b'], store['a'], store['l']//2, store['o']//2, store['n'])
        