class Solution:
    def equalFrequency(self, word: str) -> bool:

        counter = Counter(word)

        counter = list(counter.values())
        for i in range(len(counter)):
            check = counter.copy()
            check[i] -= 1
            if check[i] == 0:
                check.pop(i)
            if check == [check[-1]] * len(check):
                return True

        return False 
        


