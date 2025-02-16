class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        new_nums = nums.copy()

        for num in nums:
            new_num = 0

            while num:
                new_num *= 10
                new_num += (num % 10)
                num = num//10

            new_nums.append(new_num)
        

        return len(set(new_nums))
