class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        store = defaultdict(int)
        for cpd in cpdomains:
            count, domain = cpd.split(" ")
            domain = domain.split(".")
            for i in range(len(domain)):
                store['.'.join(domain[i:])] += int(count)
        ans = []
        for a in store:
            ans.append(str(store[a]) + " " + a)
        return ans

        return 
