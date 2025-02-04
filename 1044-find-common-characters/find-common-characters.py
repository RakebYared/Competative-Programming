class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        '''
        use default dict: char to list of count [0]*len(words)
        but edi

        '''
        common = Counter(words[0])
        for word in words[1:]:
            word_dict = Counter(word)
            for key in common:
                common[key] = min(word_dict.get(key,0), common[key])
                
        ans = []
        for letter in common:
            if common[letter] > 0:
                ans += [letter]*common[letter]
        return ans

