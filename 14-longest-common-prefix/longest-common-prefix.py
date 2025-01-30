class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = list(map(list,strs))
        stack = strs[0]
        for word in strs[1:]:
            i = 0
            while i<len(stack) and i<len(word):
                if stack[i]!=word[i]:
                    break
                i+=1
            stack = stack[:i]
        return ''.join(stack)