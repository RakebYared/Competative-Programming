class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        not_dup = set()
        for num in nums:
            if num not in not_dup:
                not_dup.add(num)
            else:
                not_dup.remove(num)
        return list(set(nums)-not_dup)
