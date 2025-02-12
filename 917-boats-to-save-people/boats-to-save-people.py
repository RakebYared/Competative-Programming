class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        min_boat = 0

        l, r = 0, len(people) -1
        
        while l < r:
            if people[l] + people[r] > limit:
                r -= 1
            
            else:
                l += 1
                r -= 1 
            min_boat += 1
        
        if l == r:
            min_boat += 1 

        return min_boat
                

            
