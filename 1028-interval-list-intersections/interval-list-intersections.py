class Solution:
    def intervalIntersection(self, first: List[List[int]], second: List[List[int]]) -> List[List[int]]:
        n = len(first)
        m = len(second)
        i, j = 0, 0
        ans = []

        while i < n and j < m:
            if first[i][1] < second[j][0]:
                i += 1
                continue
            elif  first[i][0] > second[j][1]:
                j += 1
                continue
                            
            ans.append([max(first[i][0], second[j][0]), min(first[i][1], second[j][1])])

            if first[i][1] > second[j][1]:
                j += 1
            elif first[i][1] < second[j][1]:
                i += 1
            else:
                i += 1
                j += 1

        return ans
        