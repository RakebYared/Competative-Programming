class Solution:
    def findRadius(self, ho: List[int], he: List[int]) -> int:
        ho.sort()
        he.sort()

        ans = -1
        j = 0

        for i in range(len(ho)):
            while j < (len(he)-1) and he[j] < ho[i]:
                j += 1

           
            dis = min(abs(ho[i] - he[j]), abs(ho[i] - he[j-1]))
            ans = max(dis, ans)

        return ans

