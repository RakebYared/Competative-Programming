class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,maxlen = 0, 0
        while l<len(s):
            store = set()
            r = l
            while r < len(s):
                if s[r] in store:
                    break
                store.add(s[r])
                r+=1
            maxlen = max(maxlen, len(store))
            while r<len(s) and l<r and s[l]!=s[r]:
                l+=1
            l+=1
        return maxlen

       