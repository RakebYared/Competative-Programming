class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        occurance = Counter(s)
        value = list(occurance.values())
        if value == [value[0]]*len(value):
            return True 
        else:
            return False
        