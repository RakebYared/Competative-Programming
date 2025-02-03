class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        store = defaultdict(list)

        for path in paths:
            path = path.split()
            dire = path[0]
            for files in path[1:]:
                file_name, content = files.split('(')
                store[content].append(dire +'/'+file_name)
            
            res = []
            for key in store:
                if len(store[key]) > 1:
                    res.append(store[key])
        return res

        