class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        temp = self.getRow(rowIndex-1)
        cal = []

        for i in range(len(temp)-1):
            cal.append(temp[i]+temp[i+1])

        return [1] + cal + [1]
       