class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(list)
        for a in strs:
            charcount = [0]*26
            for b in a:
                charcount[ord('a')-ord(b)]+=1
            store[tuple(charcount)].append(a)
        return store.values()
