"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        emp_list = {}
        for employee in employees:
            emp_list[employee.id] = employee
        
        def dfs(employee):

            total_imp = employee.importance

            for ID in employee.subordinates:

                sub = emp_list[ID]
                total_imp += dfs(sub)

            return total_imp
    
        return dfs(emp_list[id])


        
        