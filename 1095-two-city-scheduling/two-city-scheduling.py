class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # costs.sort(key = lambda x : max(x), reverse = True)
        costs.sort(key = lambda x : abs(x[0] - x[1]), reverse = True)
        n = len(costs)//2
        ans = 0

        a_count = n
        b_count = n
        
        for a,b in costs:
            if a < b:
                if a_count:

                    a_count -= 1
                    ans += a
                else:
                    b_count -= 1
                    ans += b
            
            else:
                if b_count:

                    b_count -= 1
                    ans += b
                else:
                    a_count -= 1
                    ans += a

           
        return ans
        