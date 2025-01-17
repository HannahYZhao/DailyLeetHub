# Time complexity: O(Nlog N)
# Space complexity: O(N)
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)] # Initialize parent array
        self.rank = [1] * n # Initialize rank array

    def find(self, x):
        # Find the root of x using path compression
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x1, x2):
        # Merge two sets using union by rank
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts)) # Create unionfind instance
        emailToAcc = {} # Email -> index of acc

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAcc:
                    uf.union(i, emailToAcc[e]) # Union accounts with common email
                else:
                    emailToAcc[e] = i
        
        emailGroup = defaultdict(list) # Index of acc -> list of emails
        for e, i in emailToAcc.items():
            leader = uf.find(i) # Find leader of account index
            emailGroup[leader].append(e) # Append email to lader's list of emails

        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0] # Get account name
            res.append([name] + sorted(emailGroup[i])) # Append name and sorted emails to result
        return res