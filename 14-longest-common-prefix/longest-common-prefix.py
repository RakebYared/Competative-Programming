class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        common_prefix = strs[0]

        for word in strs[1:]:
            i = 0

            while i<len(common_prefix) and i<len(word):
                if common_prefix[i]!=word[i]:
                    break
                i+=1

            common_prefix = common_prefix[:i]
            
        return ''.join(common_prefix)