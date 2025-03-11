class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        ans = [0]*n
        valid = True 
        i = 0

        for num in deck:  
            while not valid or ans[i%n] != 0:
                if ans[i%n] == 0:
                    valid = True
                i += 1

            ans[i%n] = num
            valid = False

        return ans


        