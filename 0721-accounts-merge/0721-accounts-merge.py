class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        '''
        
        1)a mappingform email address to account nanme
        2) form a graph 
        
        
        '''
        
        alist = defaultdict(list)
        for i in range(len(accounts)):
            for account in accounts[i][2:]:
                alist[accounts[i][1]].append(account)
                alist[account].append(accounts[i][1])
        visited = set()
        
        def dfs(node, stack):
            if node in visited:return
            stack.append(node)
            visited.add(node)
            for nei in alist[node]:
                dfs(nei, stack)
        
        res = []  
        #for i in range(len(accounts)):
        for acc in accounts:
            local_res = []
            for account in acc[1:]:
                dfs(account, local_res)
            if local_res:
                res.append([acc[0]] + sorted(local_res))
        return res