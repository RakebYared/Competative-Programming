class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l, r = 0, len(skill)-1
        total_chemistry = 0

        team = skill[r] + skill[l]

        while l<r:
            if skill[r] + skill[l] != team:
                return -1
            
            total_chemistry += skill[r] * skill[l]

            l += 1
            r -= 1
        
        return total_chemistry

