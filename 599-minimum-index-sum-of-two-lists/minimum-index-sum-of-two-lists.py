class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        '''
        min index = 
        '''
        ans = []
        store = {}
        for i in range(len(list1)):
            store[list1[i]] = i
        min_sum = float('inf')
        i = 0
        for i in range(len(list2)):
            if list2[i] in store:
                if i+store[list2[i]] < min_sum:
                    ans = [list2[i]]
                    min_sum = i+store[list2[i]]
                elif i + store[list2[i]] == min_sum:
                    ans.append(list2[i])
            
        return ans
        
