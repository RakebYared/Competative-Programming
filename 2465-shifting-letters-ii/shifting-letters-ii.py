class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0] * (len(s) + 1)

        for start, end, direction in shifts:
            prefix[start] += direction or -1
            prefix[end + 1] -= direction or -1

        for i in range(1, len(s)):
            prefix[i] += prefix[i-1]
       
        ans = []
        for i in range(len(s)):
            code = (ord(s[i]) + prefix[i] - 97) % 26
            ans.append(chr(code + 97))
        
        return ''.join(ans)
        