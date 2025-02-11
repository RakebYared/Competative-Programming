class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        '''

        '''
        store = {}
        n = len(arr)

        for i in range(len(arr)):
            store[arr[i]] = i
        
        ans = []
        for num in range(n,0,-1):
            if store[num] == num-1:
                continue 

            k = store[num] + 1
            ans.append(k)
            for key in store:
                if store[key] < k:
                    store[key] = k -1 - store[key]
            
            k = num
            ans.append(k)

            for key in store:
                if store[key] < k:
                    store[key] = k -1 - store[key]
                    
        return ans



        