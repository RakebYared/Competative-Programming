class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        store = defaultdict(int)
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                store[stack.pop()] = num
            stack.append(num)

        ans = [store[num] or -1 for num in nums1]
        return ans 