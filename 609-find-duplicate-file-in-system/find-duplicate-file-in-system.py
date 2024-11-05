class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        store = defaultdict(list)
        ans = []
        for dire in paths:
            parent, files = dire.split(" ")[0],dire.split(" ")[1:] 
            for a in files:
                file, content = a.split("(")
                content = content[:-1]
                store[content].append(parent + "/" + file)
        for a in store:
            if len(store[a])>1:
                ans.append(store[a])
        return ans




        