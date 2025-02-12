class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        icecream = [0]* (max(costs) + 1)

        for cost in costs:
            icecream[cost] += 1

        ans = 0        
        cost = 1

        while cost < len(icecream):
            if cost * icecream[cost] <= coins:
                coins -= (cost * icecream[cost])
                ans += icecream[cost]

            else:
                ans += coins // cost
                break
            
            cost += 1
       
        return ans



        