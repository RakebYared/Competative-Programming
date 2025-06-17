class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        m = 0
        for letter in s:
            if not letter.isdigit():
                m += 1 

        ans = []
  
        for num in range(1, 2**m):
            val = []

            for letter in s:
                if not letter.isdigit():
                    if num & 1:
                        val.append(letter.swapcase())
                    else:
                        val.append(letter)

                    num >>= 1

                else:
                    val.append(letter)
            
            ans.append(''.join(val))
            
        ans.append(s)
        return ans

