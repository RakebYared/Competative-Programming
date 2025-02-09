class Solution:
    def numRabbits(self, answers: List[int]) -> int: 
        rabbit_count = 0
        answer_count = Counter(answers)
        
        for answer in answer_count:
            rabbit_count += (answer + 1) * ((answer_count[answer] + answer)// (answer+1))
        
        return rabbit_count
