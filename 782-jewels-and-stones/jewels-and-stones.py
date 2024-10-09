class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        store = defaultdict(int)
        for a in stones:
            store[a]+=1
        for a in store:
            if a in jewels:
                count+=store[a]
        return count

