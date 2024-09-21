class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r=0,len(matrix)-1
        while l<=r:
            mid = (l+r)//2
            if target>=matrix[mid][0] and target<=matrix[mid][-1]:
                l,r=0,len(matrix[mid])
                while l<=r:
                    midmid= (l+r)//2
                    if matrix[mid][midmid]>target:
                        r=midmid-1
                    elif matrix[mid][midmid]<target:
                        l=midmid+1
                    else:
                        return True
                break    
            elif target<matrix[mid][0] and target<matrix[mid][-1]:
                r=mid-1
            else:
                l=mid+1

        return False







        stack=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                stack.append(matrix[i][j])
        l,r= 0,len(stack)-1
        while l<=r:
            mid = (l+r)//2
            if stack[mid]<target:
                l=mid+1
            elif stack[mid]>target:
                r=mid-1
            else:
                return True
        return False 
       