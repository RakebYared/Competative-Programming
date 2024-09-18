class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[] #to store index of num2 that is in num1
        lib = {}

        for i in range(len(nums2)):
            while stack and nums2[i]>nums2[stack[-1]]:
                lib[nums2[stack[-1]]] = nums2[i]
                stack.pop()
            if nums2[i] in nums1: stack.append(i)
        
        for i in range(len(nums1)):
            nums1[i] = lib.get(nums1[i],-1)
        
        return nums1



            
        