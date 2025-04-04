class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def compute(start, flag, num1, num2):        
            if start == n:
                return True

            i = start
            total = 0
            ans = False

            while i < n:

                total *= 10
                total += int(num[i])
                print(total)
                
                if i > start and num[start]=='0':
                    break

                if flag == 2:  
                    if (n - i) > max(2, i - start):
                        ans = compute(i+1, flag - 1, total, num2)

                elif flag == 1:
                    if (n - i) > max(1, i - start):
                        ans = compute(i+1, flag - 1 , num1,total)

                else:
                  
                    if total > num1 + num2:
                        return False
                    elif total < num1 + num2:
                        pass

                    else:
                        ans = compute(i+1,flag - 1,num2,total)
                i += 1
                if ans:
                    return True
            
            return False

        return compute(0,2,0,0)



















