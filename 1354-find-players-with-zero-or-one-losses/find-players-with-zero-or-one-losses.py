class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss = set()
        win = set()
        mult_loss = set()

        for match in matches:
            win.add(match[0])
            if match[1] in loss:
                mult_loss.add(match[1])
            else:
                loss.add(match[1])
        print(win, loss, mult_loss)
        
        return [sorted(list(win - loss)), sorted(list(loss - mult_loss))]