class Solution:
    def maskPII(self, s: str) -> str:
        
        if '@' in s:
            s = s.lower()
            name, domain = s.split('@')
            return name[0]+ '*****' +name[-1]+'@'+domain

        else:
            separator = {'+', '-', '(', ')', ' '}
            number = [a for a in s if a not in separator] 
            
            number = ''.join(number)
            if len(number) == 10:
                return '***-***-' + number[len(number)-4:]
            else:
                return '+'+'*'*(len(number)-10) + '-***-***-' + number[len(number)-4:]
            
            



        