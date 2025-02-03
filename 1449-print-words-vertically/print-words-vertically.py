class Solution:
    def printVertically(self, s: str) -> List[str]:
        '''
        len of list will be max len of word
        '''
        s = s.split(' ')
        res = []
        i = 0
        while True:
            ver_word = []
            for word in s:
                if i<len(word):
                    ver_word.append(word[i])
                else:
                    ver_word.append(' ')
            if ver_word == [' ']*len(s):
                return res  
            res.append(''.join(ver_word).rstrip())
            i+=1
                

            