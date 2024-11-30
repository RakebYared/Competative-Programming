class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        store = [""]* (max(heights)- min(heights)+1)
        factor = max(heights)
        for i, a in enumerate(heights):
            store[factor-a] = names[i]
        return [name for name in store if name != ""]