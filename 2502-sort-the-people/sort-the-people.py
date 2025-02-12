class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        person = [list(character) for character in zip(names, heights)]
        ans = [name[0] for name in sorted(person, key = lambda x : x[1], reverse = True)]
        return ans


    