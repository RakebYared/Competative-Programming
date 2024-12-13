class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if (num-3)%3:
            return []
        else:
            num = (num-3)//3 
            return [num, num+1, num+2]


        