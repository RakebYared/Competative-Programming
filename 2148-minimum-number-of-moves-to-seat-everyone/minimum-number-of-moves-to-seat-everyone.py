class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        operations = 0

        for seat,student in zip(seats, students):
            operations += abs(seat - student)
        
        return operations

        