class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        val, index = queries[0]
        nums[index] += val
        ans = [sum([num for num in nums if not num%2])]
        for q in queries[1:]:
            total = ans[-1]
            val, index = q
            
            if val%2:
                if nums[index]%2:
                    total += val + nums[index]
                else:
                    total -= nums[index]
            else:
                if not nums[index]%2:
                    total += val
            ans.append(total)
            nums[index] += val
  
        return ans


        