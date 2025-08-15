class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:

        indegree = [0]*n

        for a,b in edges:
            indegree[b] = 1

        ans = -1

        for a in range(n):
            if not indegree[a]:
                if ans == -1:
                    ans = a
                else:
                    return -1

        return ans
        