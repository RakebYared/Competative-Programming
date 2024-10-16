class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r,maxlen = 0, 0, 0
        store = set()
        while l<len(s):
            while r < len(s):
                if s[r] in store:
                    break
                store.add(s[r])
                r+=1
            maxlen = max(maxlen, len(store))
            while r<len(s) and l<r and s[l]!=s[r]:
                store.remove(s[l])
                l+=1
            l+=1
            r+=1
        return maxlen

       