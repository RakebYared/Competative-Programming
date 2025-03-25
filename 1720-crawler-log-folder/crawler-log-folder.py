class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0

        for log in logs:
            if log == './':
                continue
            elif log == '../':
                ans = ans - 1 if ans else 0
            else:
                ans += 1
        
        return ans

        