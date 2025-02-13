class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        store = set()
        l = 0
        max_length = 0

        for r in range(len(s)):
            if s[r] not in store:
                store.add(s[r])
                max_length = max(max_length, r - l + 1)
                continue
            
            while l<r:                
                store.remove(s[l])
                if s[r] == s[l]:
                    break
                l += 1
            l += 1
            store.add(s[r])
            
   
        return max_length
        