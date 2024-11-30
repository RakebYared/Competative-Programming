class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order = {x: y for y, x in enumerate(order)}
        return words == sorted(words, key= lambda x: [order[a] for a in x])
    