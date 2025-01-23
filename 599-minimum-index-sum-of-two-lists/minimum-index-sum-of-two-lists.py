class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = []
        store = {}
        for i,word in enumerate(list1):
            if word not in store:
                store[word] = i
         
        for i, word in enumerate(list2):
            if word in store:
                if not res:
                    res.append(word)
                    store[word]+=i
                elif i+store[word] < store[res[0]]: 
                    res = [word]
                    store[word]+=i
                elif i+store[word] == store[res[0]]:
                    res.append(word)
        return res