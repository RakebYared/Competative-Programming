class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = strs[0]
        for word in strs:
            i=0
            while i<len(result) and i<len(word) and result[i]==word[i]:
                i+=1
            if i<len(result): result = result[:i]
            if not result:
                return ""
        return result