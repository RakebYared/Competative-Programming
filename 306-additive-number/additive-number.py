class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def compute(start, num1, num2):

            if start == n:
                return True

            total = 0
            for i in range(start, n):

                total *= 10
                total += int(num[i])

                if i > start and num[start] == '0':
                    return False

                if total == num1 + num2 and compute(i+1, num2, total):
                    return True
                elif total < num1 + num2:
                    continue 
                else:
                    return False

            return False



        for i in range(n):
            if i > 0 and num[0] == '0':
                break

            for j in range(i+1, n-1):
                if j>i+1 and num[i+1] == '0':
                    break
                
                print(num[:i+1], num[i+1:j+1], j+1)

                if compute(j+1, int(num[:i+1]), int(num[i+1:j+1])):
                    return True

        return False



       












