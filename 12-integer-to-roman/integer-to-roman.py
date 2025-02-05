class Solution:
    def intToRoman(self, num: int) -> str:
        convertor = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        num = str(num)
        ans = []
        n = len(num)

        for i in range(len(num)):
            val = int(num[i]) 
            place = 10**(n-i-1)
            if val < 4:
                ans += [convertor[place]]*val
            elif val == 4:
                ans += [convertor[place], convertor[5*place]]
            elif val == 9:
                ans += [convertor[place], convertor[10*place]]
            
            else:
                ans.append(convertor[5*place])
                ans += [convertor[place]]*(val-5)
        return ''.join(ans)

            
            
        