class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        tens = 0
        fives = 0

        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                fives -= 1
                tens += 1
            else:
                if tens:
                    tens -= 1
                    fives -= 1
                else:
                    fives -= 3
            
            if fives < 0 or tens < 0:
                return False
        
        return True
        