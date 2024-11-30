class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        p = 0
        for a in arr2:
            for i in range(len(arr1)):
                if arr1[i] == a:
                    arr1[i], arr1[p] = arr1[p], arr1[i]
                    p+=1
        return arr1[0:p] + sorted(arr1[p:])