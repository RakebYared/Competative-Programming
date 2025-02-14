class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counter = defaultdict(int)
        l = 0
        ans = 0

        for r in range(len(fruits)):
            counter[fruits[r]] += 1

            while len(counter) > 2:
                counter[fruits[l]] -= 1
                if counter[fruits[l]] == 0:
                    counter.pop(fruits[l])
                l += 1
            
            ans = max(ans, r - l + 1)

        return ans

        