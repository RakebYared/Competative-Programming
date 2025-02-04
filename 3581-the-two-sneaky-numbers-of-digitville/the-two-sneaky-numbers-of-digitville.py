class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        visited = set()
        for num in nums:
            if num in visited:
                ans.append(num)
            else:
                visited.add(num)
        return ans
        