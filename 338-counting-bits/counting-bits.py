class Solution:
    def countBits(self, n: int) -> List[int]:
        
        
        def compute(store):
            if len(store) > n:
                return store[:n+1]

            length = len(store)

            for i in range(length):
                store.append(store[i] + 1)
            
            return compute(store)

        
        return compute([0,1])