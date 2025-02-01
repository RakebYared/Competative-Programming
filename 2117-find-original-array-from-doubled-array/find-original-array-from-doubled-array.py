class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2:
            return []
        store = defaultdict(int)
        for n in changed:
            store[n] += 1
        changed.sort()
        res = []
        for n in changed:
            if store[n]!=0: 
                if store[n*2] != 0:
                    store[n*2] -= 1
                    store[n] -= 1
                    res.append(n)
                else:
                    return []
        return res

