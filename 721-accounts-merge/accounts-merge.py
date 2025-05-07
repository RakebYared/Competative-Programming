class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        parent = {i:i for i in range(len(accounts))}

        def find(x):
            while x != parent[x]:
                x = parent[x]

            return x

        def union(x,y):
            x = find(x)
            y = find(y)

            parent[x] = y


        for i, account in enumerate(accounts):

            for acc in account[1:]:
                
                if acc in parent:
                    union(i, acc)
                else:
                    parent[acc] = i

        ans = defaultdict(set)


        for account in accounts:

            for acc in account[1:]:
                main_parent = find(acc)
                ans[main_parent].add(acc)

        # print(len(accounts), ans.keys())

        return [[accounts[i][0]] + sorted(ans[i]) for i in ans]


            