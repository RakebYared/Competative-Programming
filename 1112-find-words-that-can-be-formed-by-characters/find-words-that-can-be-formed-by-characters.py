class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        checker = [0]*26
        count = 0

        for letter in chars:
            checker[ord(letter)-97] += 1

        for word in words:
            temp = checker.copy()

            for letter in word:
                if temp[ord(letter)-97] == 0:
                    break
                temp[ord(letter)-97] -= 1
            else:
                count += len(word)
        return count

                
        