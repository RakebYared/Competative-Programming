class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        store = defaultdict(int)
        l,r,maxcount = 0, 0, 0
        counter = 0
        while r<len(s):
            while r<len(s):
                store[s[r]]+=1
                counter +=1
                if counter-max(store.values())>k:
                    break
                r+=1
            maxcount = max(maxcount, r-l)
            while counter-max(store.values())>k:
                store[s[l]]-=1
                counter-=1
                l+=1
            r+=1
        return maxcount