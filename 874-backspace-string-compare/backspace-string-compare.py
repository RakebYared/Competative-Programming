class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def find(index, word):
            count = 1
            while index > -1:
                if word[index] == '#':
                    count += 1
                else:
                    count -= 1
                
                if not count:
                    break

                index -= 1

            return index

        n = len(s)
        m = len(t)

        i, j = n-1, m-1

        while True:
            i = find(i, s)
            j = find(j, t)

            if i == -1 or j == -1:
                break

            if s[i] != t[j]:
                return False
        
            i -= 1
            j -= 1
        
        i = find(i, s)
        j = find(j, t)
        
        return True if i == -1 and j == -1 else False
